"""
Sort the columns of a csv-file

#Sort the columns of a csv-file

You get a string with the content of a csv-file. The columns are separated by semicolons.
The first line contains the names of the columns.
Write a method that sorts the columns by the names of the columns alphabetically and incasesensitive.

An example:

Before sorting:
As table (only visualization):
|myjinxin2015|raulbc777|smile67|Dentzil|SteffenVogel_79|
|17945       |10091    |10088  |3907   |10132          |
|2           |12       |13     |48     |11             |

The csv-file:
myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n
17945;10091;10088;3907;10132\n
2;12;13;48;11

----------------------------------

After sorting:
As table (only visualization):
|Dentzil|myjinxin2015|raulbc777|smile67|SteffenVogel_79|
|3907   |17945       |10091    |10088  |10132          |
|48     |2           |12       |13     |11             |

The csv-file:
Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n
3907;17945;10091;10088;10132\n
48;2;12;13;11
There is no need for prechecks. You will always get a correct string with more than 1 line und more than 1 row. All
columns will have different names.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
"""


def sort_csv_columns(csv_file_content: str) -> str:
    rows = csv_file_content.split('\n')

    header = rows[0].split(';')

    indices = sorted(range(len(header)), key=lambda i: header[i].lower())

    sorted_rows = []
    for row in rows:
        if not row:
            sorted_rows.append('')
        else:
            cols = row.split(';')
            sorted_rows.append(';'.join(cols[i] for i in indices))

    return '\n'.join(sorted_rows)


pre_sorting1 = "myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n17945;10091;10088;3907;10132\n2;12;13;48;11"
post_sorting1 = "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n3907;17945;10091;10088;10132\n48;2;12;13;11"

assert sort_csv_columns(pre_sorting1) == post_sorting1

pre_sorting2 = "Captain America;Hulk;IronMan;Thor\nhonorably;angry;arrogant;divine\nshield;greenhorn;armor;hammer\nSteven;Bruce;Tony;Thor"
post_sorting2 = "Captain America;Hulk;IronMan;Thor\nhonorably;angry;arrogant;divine\nshield;greenhorn;armor;hammer\nSteven;Bruce;Tony;Thor"

assert sort_csv_columns(pre_sorting2) == post_sorting2
