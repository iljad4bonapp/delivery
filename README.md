# Python/Flask Webapp deployment with Unit testing and Coverage

* This sample contains the completed program from the tutorial, make sure to visit the links:
[Use Azure Pipelines to build and deploy a Python web app to Azure App Service](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops) Intermediate steps are not included.


 [Python/Flask Tutorial for Visual Studio Code](https://github.com/microsoft/python-sample-vscode-flask-tutorial.git). 


**Unit Tests with Pytest**


In file **test_test1.py**

test_root to check status code of root page, expected 200

test_about to check status code of /about page expected 308

test_contact to check status code of /contact page expected 308

test_hello to check status code of dynamicaly generated /hello/test page, expected response should contain text string in response.data
