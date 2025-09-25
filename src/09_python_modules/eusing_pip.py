'''
    pip --version
run above command on prompt to know the version of pip
NOTE: Activate relative virtual environment which you are using for the project

    pip install openai
run above command on prompt to install openai package

    pip install -q langchain
it install langchain module 'silently'

    pip install anthropic==0.42
it will install anthropic package having version 0.42

    pip show anthropic
it will show the information about anthropic package with version details

    pip install --upgrade google-generativeai
it will upgrade the package google-generativeai to latest version

    pip list
it will list all the installed packages

    pip uninstall langchain
it will remove the package langchain

'''


'''
Best practices 
1) Use the latest version of pip 
upgrade pip with below command 

pyhton -m pip install --upgrade pip

2) Always use virtual envrionments

3) Record all the packages and their version required for your project with requirements.txt 
pip freeze > requirements.txt 

4) In new environment you can use requirements.txt file to setup exact dependencies of packages 
pip install -r requirements.txt 

5) Avoid adding un-necessary packages to avoid bloating of virtual environment 
'''