import datetime
import json
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def index(request):
    assets = Asset.objects.filter(owner=request.user)
    total_assets = 0
    for a in assets:
        print(a.get_asset_balance())
        total_assets = total_assets + a.get_asset_balance()
    return render(request, 'thorny_road/index.html', {'assets':assets, 'total_assets':int(total_assets)})

def str_to_date(str):
    date_str = str.split(' ')
    (year, month, day) = (date_str[0][:-1], date_str[1][:-1], date_str[2][:-1])
    completion_date = datetime.date(int(year), int(month), int(day))
    return completion_date

def add_asset(request):
    if request.method == "POST":
        collateral_name = request.POST['collateral_name']
        
        completion_date = None
        if request.POST['collateral_completion_date']:
            completion_date = str_to_date(request.POST['collateral_completion_date'])

        if collateral_name:
            try:
                c = Collateral.objects.get(name=collateral_name)
            except Collateral.DoesNotExist:
                c = Collateral.objects.create(name=collateral_name, address=request.POST['collateral_address'],
                                              old_address=request.POST['collateral_old_address'],
                                              private_area=float(request.POST['collateral_private_area']),
                                              public_area=float(request.POST['collateral_public_area']),
                                              households=int(request.POST['collateral_households']),
                                              targetholds=int(request.POST['collateral_targetholds']),
                                              completion_date=completion_date,
                                              floor_area_ratio=float(request.POST['collateral_floor_area_ratio']),
                                              building_cover_ratio=float(request.POST['collateral_building_cover_ratio']),
                                              construction_company=request.POST['collateral_construction_company'],
                                              floor=request.POST['collateral_floor'],
                                              top_floor=request.POST['collateral_top_floor'])
        else:
            return render(request, 'thorny_road/add_asset.html', {'form':request.POST, 'error':{'collateral_name':'담보물 이름을 입력해주세요.'}})

        try:
            a = Asset.objects.get(owner=request.user, collateral=c)
        except Asset.DoesNotExist:
            a = Asset.objects.create(owner=request.user, collateral=c, purchase_price=int(request.POST['asset_purchase_price']), share_rate=float(request.POST['asset_share_rate']))
    return render(request, 'thorny_road/add_asset.html', {})

def ajax_collateral_name(request):
    if request.is_ajax() and 'term' in request.GET:
        comments = Collateral.objects.filter(name__icontains=request.GET['term'])[:10]
        results = []
        for c in comments:
            c_json = {}
            c_json['id'] = c.id
            c_json['label'] = c.comment
            c_json['value'] = c.comment
            results.append(c_json)
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
    return HttpResponse()

@login_required
def detail_asset(request, aid):
    a = Asset.objects.get(owner=request.user, id=aid)
    return render(request, 'thorny_road/detail_asset.html', {'asset':a})