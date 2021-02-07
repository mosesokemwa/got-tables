Game Of Thrones - for fans across the globe

**Local set-up**
1. Create a virtual environment and install dependancies
    - For this project I used [virtual env](https://virtualenv.pypa.io/en/latest/installation.html)
    - Python 3.9.1, you can install and/or manage your python version using [pyenv](https://github.com/pyenv/pyenv)
    - Install requirements in the ```requirements.txt``` file
2. Make ```start.sh``` file executable ```chmod 755 start.sh``` and run same file to start local server
3. visit [localhost:5000](http://127.0.0.1:5000/) to view site
4. There are 3 views
    - [Characters](http://127.0.0.1:5000/characters)
    - [Books](http://127.0.0.1:5000/books)
    - [Houses](http://127.0.0.1:5000/houses)

TODO:

- [ ] Add [pagination](https://pythonhosted.org/Flask-paginate/)
- [ ] Add page sizes filtration
- [ ] Make use of flask cache