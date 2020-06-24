

class StockView(View):
    def get(self, request):
        form = StockForm()
        ctx = Stock.objects.all()
        spolka = "cdr"
        p = {"s": spolka}
        spolka2 = "pzu"
        p2 = {"s": spolka2}
        spolka3 = "bdx"
        p3 = {"s": spolka3}

        answer = requests.get("http://stooq.pl/q/", params=p3)
        # sparsowanie kodu źródłowego:
        soup = BeautifulSoup(answer.text, 'html.parser')
        answer2 = requests.get("http://stooq.pl/q/", params=p2)
        soup2 = BeautifulSoup(answer2.text, 'html.parser')
        answer3 = requests.get("http://stooq.pl/q/", params=p)
        soup3 = BeautifulSoup(answer3.text, 'html.parser')
        # try:

    # podejście 1: po id
        pzu_kurs = soup2.find("span", id=f"aq_{spolka2}_c2")
        pzu_kurs2 = float(pzu_kurs.text)
        cdr_kurs = soup3.find("span", id=f"aq_{spolka}_c1")
        cdr_kurs2 = float(znacznik_kurs.text)
        bdx_kurs = soup.find("span", id=f"aq_{spolka3}_c1")
        bdx_kurs2 = float(bdx_kurs.text)
    # print(f"Podejście 1, kurs = {kurs}")

    #
    # # podejście 2a: po napisie, a potem find
    #     znacznik_kurs = soup.find(text="Kurs").parent.find("span")
    #     kurs = float(znacznik_kurs.text)

        # if kurs:
        #     cdr_interests=Stock.objects.get(name='CDR')
        #     jednostki_cdr = cdr_interests.interests
        #     value_of_cdr = jednostki_cdr * kurs

        # znacznik_kursu = soup2.find(text="Kurs").parent.find(f"{spolka2}")
        # kurs2 = float(znacznik_kursu.text)

        # podejście 1: po id
        # spolka2_info = soup.find("span", id=f"aq_{spolka2}_c2")
        # kurs2 = float(spolka2_info.text)
        # print(f"Podejście 1, kurs = {kurs}")

    # print(f"Podejście 2a, kurs = {kurs}")
    #
    # # zmiana kursu
    #     znacznik_zmiana_bezwzgledna = soup.find("span", id=f"aq_{spolka}_m2")
    #     znacznik_zmiana_wzgledna = soup.find("span", id=f"aq_{spolka}_m3")
    #
    #     zmiana_bezwzgledna = float(znacznik_zmiana_bezwzgledna.text)
    #     zmiana_wzgledna = float(znacznik_zmiana_wzgledna.text[1:-2]) / 100


    # print(f"Podejście 1, zmiana_bezwzgledna = {zmiana_bezwzgledna}")
    # print(f"Podejście 1, zmiana_wzgledna = {zmiana_wzgledna}")
    #
    # # transakcje
    # # podejście 2b: po napisie, a potem next_element
    #     znacznik_transakcje = soup.find(text="Transakcje").next_element.next_element
    #     transakcje = int(znacznik_transakcje.text.replace(" ", ""))
    # print(f"Podejście 2b, transakcje = {transakcje}")

        return render(request, 'stock.html', {
            "cdr_kurs2":cdr_kurs2,
            "pzu_kurs2":pzu_kurs2,
            #                                   "value_of_cdr":value_of_cdr,
                                        "ctx":ctx, "form":form,
                                              # "kurs2":kurs2,
                                              "bdx_kurs2":bdx_kurs2
                                              })
        # except Exception:
        #     return render(request, 'stock.html', {"kurs":kurs, "value_of_cdr":value_of_cdr,
        #                                     "ctx":ctx, "form":form, "kurs2":kurs2})


    def post(self, request):
        form = StockForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            enter_price = form.cleaned_data['enter_price']
            interests = form.cleaned_data['interests']
            value_of = form.cleaned_data['value_of']
            price = form.cleaned_data['price']
            dividend = form.cleaned_data['dividend']
            type_of_market = form.cleaned_data['type_of_market']
            www = form.cleaned_data['www']
            Stock.objects.create(name=name, enter_price=enter_price, interests=interests, value_of=value_of,
                                 price=price,dividend=dividend,type_of_market=type_of_market,www=www)
            return redirect('stock')

