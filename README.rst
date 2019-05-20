py_curate_json
==============

Curate:
http://www.macmillandictionary.com/us/dictionary/american/curate_2
"to select items from among a large number of possibilities for other people to consume and enjoy"

Flattens a JSON record without requiring a JSON schema or invidual element mapping.

For a file with a list of JSON records (one per line), first run the curate script to create a schema.

Then run the flatten/denormalize scipt to actually flatten the JSON according to the derived schema and output as a csv file.

ToDo: configurable column sub-name delimiter
ToDo: allow retaining external branch values during the flattening/denormalization step (e.g. retain_external_branch_values=False).


The reason you see the values for columns repeated across rows is because there is a 1:1 relationship of those values to other leaf values in the document ‘tree.’  This was an intentional design decision, to allow certain common types of analytical queries to be expressed in a single, simple, performant SQL statement.

For example, if you had a document of the structure with the ‘leaf’ attributes of color and material:

document_uuid=’abc1234’
/branch1/@color=’yellow’
/branch2/sub_branch/@material=’cloth’

… there is a 1:1 relationship between color and material, so you would get a flattened, denormalized tabular structure with a redundant row such as:

document_uuid                /branch1/@color             /branch2/sub_branch/@material
---------------------                -----------------------             ----------------------------
abc1234                                yellow                                   cloth
abc1234                                yellow                                   cloth

And, if you wanted to count all the documents that have color = ‘yellow’ AND material = ‘cloth’ you could run a simple query like:

select count(distinct document_uuid) from table
where `/branch/@color` = ‘yellow’
and `/branch2/sub_branch/@material` = ‘cloth’

Alternatively, if the elements with 1:1 cardinality across branches was not repeated, you would get a table like this (maybe more like what you were expecting?):

document_uuid                /branch1/@color             /branch2/sub_branch/@material
---------------------                -----------------------             ----------------------------
abc1234                                yellow
abc1234                                                                                cloth

In this structure you could still use a simple query to get a count of documents by color, and a separate query to get results by material:

select count(distinct document_uuid) from table where `/branch1/@color` = ‘yellow’

OR

select count(distinct document_uuid) from table where `/branch2/sub_branch/@material` = ‘cloth’

But, to get a count of all documents where color=’yellow’ AND material=’cloth’ the query becomes more complex, or possibly requires multiple queries.

Maybe I’m missing something – I think this at a minimum requires a slower, more complicated self-join to express the same logic?

So, instead of this:

select count(distinct document_uuid) from table
where `/branch/@color` = ‘yellow’
and `/branch2/sub_branch/@material` = ‘cloth’

(if you want to filter on other attributes that also have a 1:1 relationship with each other, you can just add those to the where clause)

… you need something like this:

select count(distinct a.document_uuid)
from table a
join   table b
on     (a. document_uuid = b. document_uuid)
where a. `/branch1/@color` = ‘yellow’
                and b. `/branch2/sub_branch/@material` = ‘cloth’

                (for more elements that you want to use in the filter, the query syntax grows by 3x and the number of expensive self-joins increases, while performance drops, etc.)

It might still be necessary to implement more complex queries when the document structure doesn’t have a 1:1 cardinality for elements across the branches of the document structure, but the current alternative (naming repeating fields as fielda_1, fielda_2, etc.) seems far less flexible and usable to me, and inherently leads to data loss due to limiting the number of column names for each repeated element.
