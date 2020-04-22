# GPS Bulk Tool

GPS usage only!


Disclaimer:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


How to deploy:

1 - FTP to the active PROV server as ntappadm.
2 - Transfer the files to a folder like  "/var/mcp/bulk".
1 - Unzip the files as root.
2 - Inside of this folder execute "chmod 777 *" as root.



How to use:

1 - Open the config.py file with file editor.
2 - Edit the PROV user name and password.
3 - Edit the PROV URL and service.
4 - Edit the XML request of the XML field with your soap request. Your request
should be inside of triple quotes ("""). For the variable put a '$'. Program
will replace it with thea variable.
5 - If you will use counter Bulk, set counter_from and counter_until for loop
boundaries.
6 - If you will use read file bulk, put your data into the "input_file_name"
file. The program will execute the bulk for every line.
6 - Execute the program with CLI as root.
6.1 - For the counter bulk "python counterBulk.py".
6.2 - For the read file bulk "python readFileBulk.py".
7 - Check soapOut.txt and failOut.txt files for outputs.
8 - Remove all files from the server when the bulk completed!



How to use with nohup to execute at background:

nohup python -u counterBulk.py &
nohup python -u readFileBulk.py &
