# -*- coding: utf-8 -*-

import re
import urllib2
import time

class bookIf:
    def __init__(self, youth_booklist_url, author_booklist_url):
        self.youth_booklist_url = youth_booklist_url
        self.author_booklist_url = author_booklist_url

    def get_youth_group_booklist(self):
        if not self.youth_booklist_url:
            return None
        else:
            # use urllib to get html data from url
            item = 0
            total_book_list = []
            while 1:
                urlcheck = self.youth_booklist_url + "?start={0}&sort=time".format(item)
                response = urllib2.urlopen(urlcheck)
                #print "=============================================read page " + str(item/25+1) + "==================================================="
                #print urlcheck
                html_text = response.read()
                #print html_text
                #print "===============================================================raw and one line============================================================="
                #oneline_html_text = raw_html.replace('\n', ' ').replace('\r', '')
                #striped_html = raw_html.strip('\n')
                #striped_html = striped_html.strip('\r')
                #striped_html = striped_html.strip('\n')
                #print oneline_html_text
                html_text_list = html_text.splitlines()
                #print "==========================================================raw and one line========================================================="
                #print html_text_list
                book_list = []
                for i in range(0, len(html_text_list)):
                    if html_text_list[i].find('<div class="title">') >= 0:
                        #rematch = re.match(r'(http://book.douban.com/subject/)([0-9]+)(/)', html_text_list[i+1])
                        rematch = re.search('(?<=subject/)\d+', html_text_list[i+1])
                        if rematch:
                            book_id = rematch.group(0)
                            book_name = html_text_list[i+2].strip()
                            book_info = {"book_id":"", "book_name":""}
                            book_info['book_id'] = book_id
                            book_info['book_name'] = book_name
                            #print book_info
                            book_list.append(book_info)
                     
                #print "==========================================================whole book_list========================================================="        
                if book_list:
                    print book_list
                    total_book_list += book_list
                    item += 25
                    time.sleep(2)
                else:
                    break
            #print total_book_list
            return total_book_list



    def get_author_group_booklist(self):
        pass

    def get_member_booklist(self, member_id, list_type = 'desire'):
        pass

    def get_book_info(self, book_id):
        pass
