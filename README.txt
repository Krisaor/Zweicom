*--------------------------------------*
|	     ZWEICOM APP	       |
*--------------------------------------*

This app calculate the n-th term in the Fibonacci sequence.

1. How to use it

Install the pip tool using the following command:
	
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Then run the following:

	python get-pip.py

To verify the installation run the pip --version command, it should output the pip version installed in your system.

Now install Django 2.2.2 using the pip tool:

	pip install django==2.2.2

Once Django is installed, get into the root folder of the project (Zweicom/) and run the following:

	python manage.py runserver

This will start the Django server and then we just have to go to our favorite browser and put the following address:

	http://localhost:8000/fibonacci/number/put_any_number_here/

It will calculate the Fibonacci sequence of the given number.
