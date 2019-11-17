# Dev.Art

A website displaying a user's art in a professional manner. 
All content can be changed/ deleted or new content added via the admin page.

The site makes use of Django/Python and Bootstrap4

*The Carousel images needs to be 774px high and 200 px wide*
Uploaded posts with artwork may be either landscape or portrait dimmensions.

In 'main/urls.py' at the end of the block bracket there is are lines:" + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# simply used static during developmental stage to ensure media file are accessible, not used during deployment." which need to be removed during deployment

Contact me: dutoitdevon@gmail.com for help/ enquiries or general info
