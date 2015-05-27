# -*- coding: utf-8 -*-

import re
import urllib2

class bookIf:
    def __init__(self, youth_booklist_url, author_booklist_url):
        self.youth_booklist_url = youth_booklist_url
        self.author_booklist_url = author_booklist_url

    def get_youth_group_booklist(self):
        if not self.youth_booklist_url:
            return None
        else:
            # use urllib to get html data from url
            i = 0
            doulist_content = []
            while 1:
                urlcheck = self.youth_booklist_url + "?start={0}&sort=time".format(i)
                response = urllib2.urlopen(urlcheck)
                #print "=============================================read page " + str(i/25+1) + "==================================================="
                #print urlcheck
                #print response.read()
                # use re.findall to get a raw match (as douban.com show twice a input list.)
                # as the time to remove duplicate accumulates, better way is match only once,
                # and then cut unwanted parts (of course its an better algorithm as it is O(n))
                book_url_in_page = re.findall('http://book.douban.com/subject/[0-9]*/', response.read())
                if not book_url_in_page:
                    break
                else:
                    self.__remove_duplicate_element(book_url_in_page)
                    for book_url in book_url_in_page:
                        doulist_content.append(book_url)
                    i += 25
                # limited function now: only first 25 book in a long list is get.

                self.__remove_duplicate_element(doulist_content)  
                return doulist_content



    def get_author_group_booklist(self):
        pass

    def get_member_booklist(self, member_id, list_type = 'desire'):
        pass

    def get_book_info(self, book_id):
        pass

    # remove duplicate of a list
    def __remove_duplicate_element(self, list):
        i = 0
        while i <= len(list) - 1:
            j = i + 1
            while j <= len(list) - 1:
                if list[i] == list[j]:
                    del list[j]
                j += 1
            i += 1