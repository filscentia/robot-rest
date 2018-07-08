import json

import falcon


class Motor(object):

    def on_post(self, req, resp, side):       
        if req.media['state']  == 1:
            print forward
            
        print('POST {} {}'.format(side, req.media['state']))

    def on_get(self, req, resp, side):
        print(side)
        # doc = {         
        # }
        # if side == "left":
        #     doc.left = "on"
        # else if side == "right"
        #     doc.right = "on"
        # else
        #     doc.both="on"
            
            
        

        # # Create a JSON representation of the resource
        # resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200