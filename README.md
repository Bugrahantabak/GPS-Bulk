# GPS Bulk Tool

Only for the GPS usage!


Disclaimer:

This SOFTWARE PRODUCT is provided by THE PROVIDER "as is" and "with all faults.
" THE PROVIDER makes no representations or warranties of any kind concerning
the safety, suitability, lack of viruses, inaccuracies, typographical errors,
or other harmful components of this SOFTWARE PRODUCT. There are inherent
dangers in the use of any software, and you are solely responsible for
determining whether this SOFTWARE PRODUCT is compatible with your equipment
and other software installed on your equipment. You are also solely
responsible for the protection of your equipment and backup of your data, and
THE PROVIDER will not be liable for any damages you may suffer in connection
with using, modifying, or distributing this SOFTWARE PRODUCT.


How to deploy:

1 - FTP to the PROV server as ntappadm.
2 - Transfer the files to a folder like  "/var/mcp/bulk".
1 - Unzip the files.
2 - Inside of this folder execute "chmod 777 *"



How to use:

1 - Open the config.py file by file editor.
2 - Edit the PROV user name and password.
3 - Edit the PROV URL and service.
4 - Edit the XML request of the XML field with your soap request. Your request
should be inside of triple quotes ("""). For variable put a '$'. The program
will replace it with a variable.
5 - If you will use counter Bulk, set counter_from and counter_until for loop
boundaries.
6 - If you will use read file bulk, set your data into the "input_file_name"
file. The program will execute the bulk for every line.
6 - Execute the program with CLI.
6.1 - For the counter bulk "python counterBulk.py".
6.2 - For the read file bulk "python readFileBulk.py".
7 - Check soapOut.txt and failOut.txt files for outputs.
8 - Remove all files from the server when the bulk completed!
