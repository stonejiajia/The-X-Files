<!DOCTYPE HTML>
<html>
	<head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <!--jquery-->
        <script src=jquery/jquery-1.11.3.min.js></script>
        <!-- jquery mobile-->        
		<link rel=stylesheet href=jquery-mobile/css/jquery.mobile-1.4.5.css>
		<script src=jquery-mobile/js/jquery.mobile-1.4.5.js></script>
        <!--highcharts-->
		<script src=hightcharts/highcharts.js></script>
        <!-- Scrollz -->
        <link rel=stylesheet href=jquery-scrollz/jquery.scrollz.css>
        <script src=jquery-scrollz/jquery.scrollz.min.js></script>
		<script type="text/javascript">
            // Next page index loaded
            var nextPageIndex = 0;
            
            // Indicates if new entries loading is in progress
            var loading = false;
        
            // Load more function        
            function loadMore() {
                
                if (!loading) {
                
                    loading = true;
                    protocol = document.location.protocol == 'file:' ? 'http:' : document.location.protocol;
                    url = 'cp42.sinaapp.com';
                    //url = 'http://zippy1978.tumblr.com/rss';
                    $.ajax({
                    type: "GET",
                    //url: protocol + '//ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=1000&callback=?&q=' + encodeURIComponent(url),
                    url: protocol + encodeURIComponent(url),
                    //dataType: 'json',
                    dataType: 'text',
                    error: function(){
                        loading = false;
                    },
                    success: function(xmlbook){
                        
                        var targetList = $('#items');
                        
                        
                        /*values = xml.responseData.feed.entries;
                        
                        // First page
                        if (nextPageIndex == 0) {
                            targetList.empty();
                        }

                        $.each(values, function() {
                            targetList.append('<li><img class="ui-li-icon" src="https://lh5.googleusercontent.com/-T4SN-W1_Gkk/AAAAAAAAAAI/AAAAAAAAAv0/xRQBInxIzJo/s120-c/photo.jpg"/><h3 class="wrapping-new-line"><a href="' + this.link + '">' + this.title + '</a></h3><p class="wrapping-new-line">' + this.contentSnippet + '<a href="' + this.link + '">read more</a></p><p class="date">' + this.publishedDate + '</p></li>');
                        });

                        targetList.listview("refresh");*/

                        //var txt = document.getElementById("textscroller").value;
                        document.getElementById("textscroller").innerHTML = xmlbook;
                        //if (loading == ture) {
                        //   list = ['机器人叛乱', '创造力', '从0到1', '失控', '经验的疆界']
                        //   $('#bookchart').highcharts();
                        //   }
                        list_book = ['机器人叛乱', '创造力', '失控' , '经验的疆界', '神们自己' , '心思大开' ];
                    
                        var str="从0到1"
                        var bookcut = str.substr(0,2);
                        list_book.push(bookcut);
                        list1.push(5);
                           
                        //var book ＝ "经验的疆界"
                        //var bookcut = book.substr(0,2);
                        //list.push(bookcut1);
                        showBookChart();

                        // Hide pull header after first page is loaded
                        if (nextPageIndex == 0) {
                            $('#container').scrollz('hidePullHeader');
                        }
                        
                        nextPageIndex++;
                        loading = false;
                    }
                });
            
                }
                
            }

            // Load initial items
            loadMore();         

            $(document).on('pulled', '#container', function() {
                 // Reset page index
                nextPageIndex = 0;
                
                // Reload
                loadMore();
            });
            list_book = ['Books', 'Lover', 'Rebel of Robots', 'Story', 'Element of Styles' , 'sss']
            list1 = [3,6,4,7,8,7]
            function showBookChart() {
                $('#bookchart').highcharts({
                    chart: {
                        type: 'bar'
                    },
                    title: {
                        text: '本周热点图书'
                    },
                    subtitle: {
                        text: 'in this week'
                    },
                    xAxis: {
                        categories: list_book //['Books', 'Lover', 'Rebel of Robots', 'Story', 'Element of Styles']
                    },
                    yAxis: {
                        min: 0,
                        title: {
                            text: '标记人数'
                        }
                    },
                    tooltip: {
                        valueSuffix: '人'
                    },
                    plotOptions: {
                        series:{
                            stacking: 'normal'
                        }
                    },
                    legend: {
                        reversed: true
                    },
                    series: [{
                        name: '已读',
                        data: list1//[5,3,4,7,2]
                    //}, {
                     //   name: '在读',
                     //   data: [2,2,3,2,1]
                    //}, {
                     //   name: '想读',
                     //   data: [3,4,4,2,5]
            	    }]
                });
            }

            $(showBookChart);
            
            
            //list = ['机器人叛乱', '创造力', '从0到1', '失控', '经验的疆界']
</script>

<style type="text/css">
#textscroller {
    /*position: absolute; */
    z-index: 1;
    top: 400px;
    bottom: 48px;
    left: 0;
    width: 100%;
    background: #fff;
    overflow: hidden;
}

#bookchart {
    /*position: absolute; */ /*This code will block pull-to-refresh function*/ 
    z-index: 1;
    top: 0px;
    bottom: 48px;
    left: 0;
    width: 100%;
    height: 400px;
    background: #fff;
    overflow: hidden;
}

p {
    font-size: 16px;
    padding: 1.2em;
    line-height: 200%;
}
</style>
</head>

<body>

<div id="container"  data-role="content" data-scrollz="pull">
    <div id="bookchart"></div>
    <div id="textscroller" >
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

</div>
</body>
</html>
