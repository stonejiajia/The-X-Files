# -*- coding: utf-8 -*-

import re
import urllib2
import time

class bookIf:
    def __init__(self, youth_booklist_url, author_booklist_url):
        self.youth_booklist_url = youth_booklist_url
        self.author_booklist_url = author_booklist_url

    def get_group_booklist(self, group_id):
        if group_id != "youth" and group_id != "author":
            return None
        
        if group_id == "youth":
            if not self.youth_booklist_url:
                return None           
            else:
                return self.__get_douban_booklist(self.youth_booklist_url)

        if group_id == "author":
            if not self.author_booklist_url:
                return None           
            else:
                return self.__get_douban_booklist(self.author_booklist_url)
            


    def get_member_booklist(self, member_id, list_type = 'wish'):
        root_url = "http://book.douban.com/people/" + member_id
        if list_type == "wish":
            full_url = root_url + "/wish"
            return self.__get_douban_people_readlist(full_url, False) # for wish list, book rating is meaningless, False for not get rating.
        elif list_type == "reading":
            full_url = root_url + "/do"
            return self.__get_douban_people_readlist(full_url)
        elif list_type == "done":
            full_url = root_url + "/collect"
            return self.__get_douban_people_readlist(full_url)
        else:
            return None

    def get_book_info(self, book_id):
        pass
    
    def __get_douban_booklist(self, url):
        item = 0
        total_book_list = []
        while True:
            full_url = url + "?start={0}&sort=time".format(item)
            response = urllib2.urlopen(full_url)
            #print "=============================================read page " + str(item/25+1) + "==================================================="
            #print urlcheck
            html_text = response.read()
            #print html_text
            #print "===============================================================raw and one line============================================================="
            #oneline_html_text = raw_html.replace('\n', ' ').replace('\r', '')
            #striped_html = raw_html.strip('\n')
            #striped_html = striped_html.strip('\r')
            #striped_html = striped_html.strip('\n')
            html_text_list = html_text.splitlines()

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
                       
            if book_list:
                #print book_list
                total_book_list += book_list
                item += 25
                time.sleep(1) #sleep 1 second to avoid being blocked by douban.com for frequent access.
            else:
                break
        #print total_book_list
        return total_book_list
    
    def __get_douban_people_readlist(self, url, WANT_RATING = True):
        item_num = 0
        total_book_list = []
        
        while True:
            #print "=============================================read page " + str(item_num/15+1) + "==================================================="
            full_url = url + "?start={0}&sort=time".format(item_num)
            response = urllib2.urlopen(full_url)
            html_text = response.read()
            html_text_list = html_text.splitlines()

            book_list = []
            got_book_title = False    # used for search book rating. only after a book title is found, book rating is to be searched.
            
            for html_line in html_text_list:
                book_info = {"book_id":"", "book_name":"", "rating":0}
                
                if WANT_RATING and got_book_title:
                    rate_search = re.search('(<span class="rating)(\d)(-t"></span>)', html_line)
                    if rate_search:
                        book_rating = rate_search.group(2)
                        book_list[len(book_list)-1]["rating"] = int(book_rating)
                        got_book_title = False
                        continue

                search_result = re.search('(http://book.douban.com/subject/)(\d+)(/)(.+)(title=")(.+)(")', html_line)
                if search_result:
                    book_id = search_result.group(2)
                    book_name = search_result.group(6)
                    
                    book_info['book_id'] = book_id
                    book_info['book_name'] = book_name
                                    
                    book_list.append(book_info)                        
                    got_book_title = True
                        
            if book_list:
                total_book_list += book_list
                item_num += 15
                print book_list
                time.sleep(1) #sleep 1 second to avoid being blocked by douban.com for frequent access.
            else:
                break        
        return total_book_list

