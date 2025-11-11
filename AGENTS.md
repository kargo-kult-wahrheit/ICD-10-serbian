# mkb-scrape
scrape icd-10 in serbian from stetoskop
Ministry of health of Serbia has published the ICD-10 in serbian (MKB-10), but it's a pdf and not searchable. 
They do have a website, but no way to download the whole list, on which our department of public health at Batut relies on. 
We asked the ministry, and they agreed that we can scrape the website for the list, if we know how to do  it. 
You should write a python script, dockerize it, which I can  run on  a local machine  to scrape this website: https://www.stetoskop.info/mkb for all MKB-10 info, and then put it in a csv, in order.

So, your tasks  are:
1. create a  python script  that can scrape the ICD-10 data from https://www.stetoskop.info/mkb, and  put it in order in a csv.
   1a: data should be formatted as follows:
   code|description, serbian|description, latin
   A00|Kolera NOVA|Cholera
   A00.0|Kolera, uzročnik Vibrio cholerae 01,biotip cholerae|Cholera classica
   etc.
2. create a docker container with all the dependencies etc. that will allow me to use the script on our department's computer
