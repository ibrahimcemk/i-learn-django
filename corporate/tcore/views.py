from django.shortcuts import render

def website_info(request):
    context_data={
        'name': 'İbrahim Cem',
        'company':'ibozivyon',
        'website':'ibrahimcemkeles.com',
    
    }

    return render(request,'ibrahimcemkeles.html',context_data)