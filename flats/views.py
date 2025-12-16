from django.db.transaction import commit
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from flats.models import Flat, DealRequest
from django.contrib.auth.decorators import login_required
from flats.forms import FlatForm, DealRequestForm


def flats_list(request):
    all_flats = Flat.objects.filter(available=True)
    return render(request, 'flats_list.html', context={
        'all_flats': all_flats
    })

def flat_detail(request, flat_id):
    flat_from_db = get_object_or_404(Flat, id=flat_id)
    return render(request, 'flat_detail.html', context={
        'flat': flat_from_db
    })

@login_required
def flat_create(request):
    if not request.user.is_owner():
        return redirect("flats:flats_list")

    if request.method == "POST":
        form = FlatForm(request.POST, request.FILES)
        if form.is_valid():
            flat = form.save(commit=False)
            flat.owner = request.user
            flat.save()
            return redirect("flats:flat_detail", flat_id=flat.id)
    else:
        form = FlatForm()

    return render(request, "flat_create.html", context={"form": form})


@login_required
def flat_edit(request, flat_id):
    flat = get_object_or_404(Flat, id=flat_id, owner=request.user)

    if request.method == "POST":
        form = FlatForm(request.POST, request.FILES, instance=flat)
        if form.is_valid():
            form.save()
            return redirect("flats:flat_detail", flat_id=flat.id)
    else:
        form = FlatForm(instance=flat)

    return render(request, "flat_create.html", context={"form": form})

@login_required
def flat_delete(request, flat_id):
    flat = get_object_or_404(Flat, id=flat_id, owner=request.user)

    if request.method == "POST":
        flat.delete()
        return redirect("flats:flats_list")

    return render(
        request,
        "flat_confirm_delete.html",
        context={
            "flat": flat
        }
    )

@login_required
def send_deal_request(request, flat_id):
    flat = get_object_or_404(Flat, id=flat_id)

    if not request.user.is_seeker():
        return redirect("flats:flat_detail", flat_id=flat_id)

    if request.method == "POST":
        form = DealRequestForm(request.POST)
        if form.is_valid():
            deal_request = form.save(commit=False)
            deal_request.seeker = request.user
            deal_request.flat = flat
            deal_request.save()
            return redirect("flats:flats_list")
    else:
        form = DealRequestForm()

    return render(request,
                  "deal_request.html",
                  context={
                      "form": form,
                      "flat": flat
                  })


@login_required
def owner_deals_requests_list(request):
    if not request.user.is_owner():
        return redirect("flats:flats_list")

    all_requests = (DealRequest.objects
                    .select_related("flat", "seeker")
                    .filter(flat__owner=request.user))

    return render(request, "owner_deals_requests.html",
                  context={"all_requests": all_requests})