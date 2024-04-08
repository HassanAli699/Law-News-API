# Law-News-API
This is the Api to scrape law news from a site called Courting The Law. This is a Pakistani Website that provides information regarding law internationally and nationally.

-------------
**END-POINT:**

http://YOUR_LOCAL_URL_HERE/get_news

**PARAMETERS:**

num_pages (Specifies the number of pages you want to scrape from the site) 

page (This is a paginated API. This parameter tell you which page you are on the response)

per_page (Specifies how many articles are on a single page)

**Default Values**

num_pages = 1 Type: *INT*

page = 1 Type: *INT*

per_page = 10 Type: *INT*

--------------------

**EXAMPLE RESPONSE**

*http://192.168.1.6:5000/get_news?num_pages=5&page=1&per_page=10*

![image](https://github.com/HassanAli699/Law-News-API/assets/119949006/c035c6f9-4c8c-4388-98dc-6c9d47b5a916)

![image](https://github.com/HassanAli699/Law-News-API/assets/119949006/19eec7ca-4704-481c-a184-0e802c34c016)





