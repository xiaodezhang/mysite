import markdown2
import os
import sched,time

sch = sched.scheduler(time.time,time.sleep)

def update_md(sc):
    #app_name = ["note","dic"]
    app_name = ["note","dic","mysite"]
    #app_name = ["note","dic","blog"]
    for name in app_name:
        md_file = name+"/templates/"+name+"/"+name+".md"
        index_file = name+"/templates/"+name+"/index.html"
        index_cache_file = name+"/templates/"+name+"/index_cache"

        html = markdown2.markdown_path(md_file)
        if os.path.isfile(index_cache_file):
            s_cache = open(index_cache_file).read()
        else:
            s_cache = open(index_file).read()
        s = s_cache.replace('{% md "'+name+'.md" %}',html)
        f_cache = open(index_cache_file,'w')
        f = open(index_file,'w')
        f_cache.write(s_cache)
        f.write(s)
        f_cache.close()
        f.close()
    sch.enter(5,1,update_md,(sc,))
sch.enter(5,1,update_md,(sc,))
sch.run()
