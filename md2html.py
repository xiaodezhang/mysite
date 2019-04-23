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
        index_cache_file = name+"/templates/"+name+"/index_cache.html"

        html = markdown2.markdown_path(md_file)
        if os.path.isfile(index_cache_file):
            # we need to set the codings on windows
            s_cache = open(index_cache_file,'r',encoding='utf-8').read()
        else:
            s_cache = open(index_file,'r',encoding='utf-8').read()
        s = s_cache.replace('{% md "'+name+'.md" %}',html)
        f = open(index_file,'w',encoding='utf-8')
        f.write(s)
        f.close()
    sch.enter(5,1,update_md,(sc,))
sch.enter(5,1,update_md,(sch,))
sch.run()
