from .autoload import *
def blogweb_pages(request,slug):
    temp_path = 'blogweb/'+slug+'.html'
    status = template_exist(temp_path)
    if status == False:
        temp_path = 'blogweb/404.html'
    return render(request,temp_path,{'slug':slug})
    
def template_exist(templatepath):    
    try:
        template.loader.get_template(templatepath)
        return True
    
    except:
        return False
    