# Milo Django Test 

### Deployment Instructions

Assuming you are on Linux and you have python3 and git installed.

```bash
mkdir milotest
virtualenv env -p python3
source env/bin/activate
git clone git@github.com:olexiy-logvinov/milo.git
cd milo
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver

```
Now you should be able to [load the home page](http://127.0.0.1:8000/)

### Release Notes
#### v1.0
* extended User model with birthday and randint fields.
* created views for:
   * [list of all users](http://127.0.0.1:8000/)
   * single user
   * [creating a new user](http://127.0.0.1:8000/create_user/)
   * deleting user
   * editing user

* created two template tags - "allowed" and "bizzfuzz"   
* added a [link for downloading users csv file](http://127.0.0.1:8000/export_to_csv) on a home page. Exporting users to a native xlsx file format would require installing **openpyxl** library, so I decided to save time and use a standard **csv** library instead.

### Additional Info
* Please find screen images in the screenshots directory.
* users.csv can be found in the root folder.   
   