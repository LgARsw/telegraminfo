import flet as ft
import telethon
from telethon.sync import TelegramClient
from telethon import functions, types
import python_socks
from python_socks.async_.asyncio import Proxy
import asyncio
import json
import random
import traceback
import time
import threading
import json
import os
from threading import Semaphore


def main(page: ft.Page):
    def find_option(option_name):
        for option in d1.options:
            if option_name == option.key:
                return option

        return None

    def find_option1(option_name1):
        for option1 in d.options:
            if option_name1 == option1.key:
                return option1
        return None

    def pick_files_result1(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else " "
        )
        global sel
        sel = selected_files.value
        selected_files.update()

    pick_files_dialog1 = ft.FilePicker(on_result=pick_files_result1)
    selected_files = ft.Text()

    def pick_files_result2(e: ft.FilePickerResultEvent):
        selected_files1.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else " "
        )
        global sel1
        sel1 = selected_files1.value
        selected_files1.update()

    pick_files_dialog2 = ft.FilePicker(on_result=pick_files_result2)
    selected_files1 = ft.Text()

    def pick_files_result3(e: ft.FilePickerResultEvent):
        selected_files2.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else " "
        )
        global sel2
        sel2 = selected_files2.value
        selected_files2.update()

    pick_files_dialog3 = ft.FilePicker(on_result=pick_files_result3)
    text1 = ft.Text()
    selected_files2 = text1

    def pick_files_result4(e: ft.FilePickerResultEvent):
        selected_files3.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else " "
        )
        global sel3
        sel3 = selected_files3.value
        selected_files3.update()

    pick_files_dialog4 = ft.FilePicker(on_result=pick_files_result4)
    selected_files3 = ft.Text()
    button_pick = ft.Row(
        [
            ft.ElevatedButton(
                "Файл.txt с ссылками на группы, с которых собираем подписчиков с историями",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=lambda _: pick_files_dialog1.pick_files(
                    allow_multiple=True
                ),
            ),
            selected_files,
        ]
    )

    button_add = ft.Row(
        [
            ft.ElevatedButton(
                "Файл.txt для сохранения никнеймов подписчиков с историями",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=lambda _: pick_files_dialog2.pick_files(
                    allow_multiple=True
                ),
            ),
            selected_files1,
        ]
    )
    button_select = ft.Row(
        [
            ft.ElevatedButton(
                "Файл.txt с никнеймами людей для просмотра и лайкинга их историй",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=lambda _: pick_files_dialog3.pick_files(
                    allow_multiple=True
                ),
            ),
            selected_files2,
        ]
    )
    button_pick1 = ft.Row(
        [
            ft.ElevatedButton(
                "Файл.txt с ссылками на группы для просмотров и лайков историй подписчиков",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=lambda _: pick_files_dialog4.pick_files(
                    allow_multiple=True
                ),
            ),
            selected_files3,
        ]
    )

    def update(e):
        generate()
        page.clean()
        page.add(*pan_static)

    button_update = ft.FilledButton(text="Обновить", on_click=update)

    def stop3(e, namee):
        global name_stop
        name_stop = namee
        print(namee)

    def generate():
        global pan_static

        gl = 1
        pan_static = (button_update, ft.Text(f""))
        amount = []
        with open("base.json", "r") as cin:
            amount = json.load(cin)
        gl = 0
        for i in amount:
            try:
                file = open(f'{i["name"]}.json', 'r+')
                status = []
                with open(f"{i["name"]}.json", "r") as pin:
                    data = pin.read()
                status = json.loads(data)
                for b in status:
                    pan_static = pan_static + (ft.Container(
                        content=ft.Text(
                            f"Имя: {i["name"]}\nСтатус: {b["status"]}\nКоличество просмотренных историй: {b["watches"]}\nКоличество лайков: {b["likes"]}\nКоличество найденных людей: {b["chel"]}\nКоличество просмотренных групп: {b["chan"]}"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.BLUE,
                        width=320,
                        height=185,
                        border_radius=10,
                    ), ft.FilledButton(text="Остановить парсинг", on_click=lambda e, namee=i["name"]: stop3(e, namee)),
                                               ft.FilledButton(text="Остановить просмотр и лайки историй",
                                                               on_click=lambda e, name_stop1=i["name"]: stoparse(e,
                                                                                                                 name_stop1)),
                                               ft.FilledButton(text="Остановить парсинг, просмотр и лайки историй",
                                                               on_click=lambda e, name_stop2=i["name"]: stoppp(e,
                                                                                                               name_stop2)),
                                               ft.FilledButton(text="Очистить статистику",
                                                               on_click=lambda e, name1=i["name"]: stat(e, name1)))

            except IOError:
                file = open(f'{i["name"]}.json', 'w+')
                res = []
                pattern1 = {"status": "offline", "watches": 0, "likes": 0, "chel": 0, "chan": 0}
                res.append(pattern1)
                with open(f"{i["name"]}.json", "w") as min:
                    json.dump(res, min, ensure_ascii=False)
                status = []
                with open(f"{i["name"]}.json", "r") as pin:
                    data = pin.read()

                status = json.loads(data)
                for b in status:
                    pan_static = pan_static + (ft.Container(
                        content=ft.Text(
                            f"Имя: {i["name"]}\nСтатус: {b["status"]}\nКоличество просмотренных историй: {b["watches"]}\nКоличество лайков: {b["likes"]}"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.BLUE,
                        width=320,
                        height=185,
                        border_radius=10,
                    ), ft.FilledButton(text="Остановить парсинг", on_click=lambda e, namee=i["name"]: stop3(e, namee)),
                                               ft.FilledButton(text="Остановить просмотр и лайки историй",
                                                               on_click=lambda e, name_stop1=i["name"]: stoparse(e,
                                                                                                                 name_stop1)),
                                               ft.FilledButton(text="Остановить парсинг, просмотр и лайки историй",
                                                               on_click=lambda e, name_stop2=i["name"]: stoppp(e,
                                                                                                               name_stop2)),
                                               ft.FilledButton(text="Очистить статистику",
                                                               on_click=lambda e, name1=i["name"]: stat(e, name1)))

    amount = []
    with open("base.json", "r") as cin:
        amount = json.load(cin)
    for am in amount:
        try:

            status = []
            with open(f"{am["name"]}.json", "r") as pin:
                data = pin.read()
            status = json.loads(data)
            for b in status:
                if b["status"] != "offline":
                    status.remove(
                        {"status": b["status"], "watches": b["watches"], "likes": b["likes"], "chel": b["chel"],
                         "chan": b["chan"]})
                    status.append({"status": "offline", "watches": b["watches"], "likes": b["likes"], "chel": b["chel"],
                                   "chan": b["chan"]})
                    with open(f"{am["name"]}.json", "w") as pout:
                        json.dump(status, pout, ensure_ascii=False)
        except IOError:
            file = open(f'{am["name"]}.json', 'w+')
            res = []
            pattern1 = {"status": "offline", "watches": 0, "likes": 0, "chel": 0, "chan": 0}
            res.append(pattern1)
            with open(f"{am["name"]}.json", "w") as min:
                json.dump(res, min, ensure_ascii=False)

    # кол-во пользователей
    gl = 0
    global pan_static

    pan_static = (button_update, ft.Text(f""))

    generate()

    page.scroll = "always"
    page.title = "Reels_liker"
    d = ft.Dropdown()
    d1 = ft.Dropdown()
    list = []
    with open("base.json", "r") as bin:
        list = json.load(bin)
    print(list)
    for j in list:
        d.options.append(ft.dropdown.Option(j["name"]))
    for j in list:
        d1.options.append(ft.dropdown.Option(j["name"]))
    greetings = ft.Column()

    def navigate(e):
        global pagee
        pagee = ""
        page.clean()
        if page.navigation_bar.selected_index == 0:
            page.add(*pan_auth)
            pagee = "*pan_auth"
        elif page.navigation_bar.selected_index == 1:
            page.add(*pan_work)
            pagee = "pan_work"
        elif page.navigation_bar.selected_index == 2:
            page.add(*pan_static)
            pagee = "pan_static"

    def go(e):

        global name_stop
        name_stop = "none"
        thread1 = threading.Thread(target=start)
        thread1.run()

    def GO(e):
        global a2
        a2 = "none"
        thread3 = threading.Thread(target=start2)
        thread3.run()

    def GO1(e):
        global a2
        a2 = "none"
        thread4 = threading.Thread(target=start3)
        thread4.run()

    def stoparse(e, name_stop1):
        global a1
        a1 = name_stop1
        print(name_stop1)
        pass

    def stoppp(e, name_stop2):
        global a2
        a2 = name_stop2
        pass

    def stat(e, name1):
        lis = []
        with open(f"{name1}.json", "r") as cin:
            lis = json.load(cin)
        for i in lis:
            status = i["status"]
            watches = i["watches"]
            likes = i["likes"]
            chel = i["chel"]
            chan = i["chan"]
        pattern1 = {"status": status, "watches": watches, "likes": likes, "chel": chel, "chan": chan}
        pattern2 = {"status": status, "watches": 0, "likes": 0, "chel": 0, "chan": 0}
        lis.remove(pattern1)
        lis.append(pattern2)
        with open(f"{name1}.json", "w") as cout:
            json.dump(lis, cout, ensure_ascii=False)

        generate()

    def parse(e):
        global a1
        a1 = "none"
        thread1 = threading.Thread(target=start1)
        thread1.run()

    def parse1(e):
        global a1
        a1 = "none"
        thread5 = threading.Thread(target=start4)
        thread5.run()

        pass

    def start3():
        global a2
        if tim.value.isdigit():

            textt = tim.value
            print(int(textt))
        else:
            list2 = tim.value.split("-")
            textt = random.randint(int(list2[0]), int(list2[-1]))
        print(int(textt))
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("AAA")
        a = []
        text = f"{d.value}"
        with open("base.json", "r") as cin:
            a = json.load(cin)

        try:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
                    zero = j["zero"]
                    one = j["one"]
                    two = j["two"]
                    three = j["three"]
            client = TelegramClient(name, apiid, apihash,
                                    proxy=(python_socks.ProxyType.HTTP, zero, one, True, two, three))
        except:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
            client = TelegramClient(name, apiid, apihash)

        client.connect()

        f = open(f"{sel3}", "r")
        txt = f.read().splitlines()
        print(txt)
        chan = 0
        list = []
        list1 = []
        for rt in txt:
            try:
                chan += 1
                channel = client.get_entity(rt)
                all_participants = client.get_participants(channel)

                status = []

                with open(f"{name}.json", "r") as din:
                    status = json.load(din)
                for j in status:
                    pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                               "chan": j["chan"]}
                    pattern1 = {"status": "Идет парсинг", "watches": j["watches"], "likes": j["likes"],
                                "chel": j["chel"], "chan": j["chan"]}
                status.remove(pattern)
                status.append(pattern1)
                with open(f"{name}.json", "w") as kin:
                    json.dump(status, kin, ensure_ascii=False)
                generate()
                if pagee == "pan_static":
                    page.clean()
                    page.add(*pan_static)
                page.update()
                list = []
                list1 = []

                flog = 0
                for i in range(int(stor.value)):
                    flog += 1

                    list.append(flog)
                print(list)
                print(list[-1])
                chel = 0
                liker = 0
                storyy = 0
                for i in all_participants:
                    try:
                        time.sleep(int(tim.value))
                        if name == a2:
                            print("Right")
                            client.disconnect()
                            with open(f"{name}.json", "r") as din:
                                status = json.load(din)
                            for j in status:
                                pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"],
                                           "chel": j["chel"], "chan": j["chan"]}
                                pattern1 = {"status": "offline", "watches": j["watches"], "likes": j["likes"],
                                            "chel": j["chel"], "chan": j["chan"]}
                            status.remove(pattern)
                            status.append(pattern1)
                            with open(f"{name}.json", "w") as kin:
                                json.dump(status, kin, ensure_ascii=False)
                            generate()
                            if pagee == "pan_static":
                                page.clean()
                                page.add(*pan_static)
                            page.update()
                            return
                        if (
                                not i.stories_unavailable and
                                not i.stories_hidden and
                                i.stories_max_id
                        ):

                            res = client(
                                functions.stories.ReadStoriesRequest(
                                    peer=i.id,
                                    max_id=i.stories_max_id
                                ))
                            if i.username == None:
                                pass
                            else:
                                print(i.username)

                                result = client(functions.stories.GetPeerStoriesRequest(
                                    peer=f'@{i.username}'
                                ))
                                fl = 0
                                fla = 0

                                for re in result.stories.stories:
                                    fl += 1

                                    if fl >= list[-1]:
                                        fla += 1
                                if fla > 0:
                                    storyy = 0
                                    for re in result.stories.stories:
                                        storyy += 1
                                        print(re.id)
                                        list1.append(re.id)

                                    random.shuffle(list)
                                    for jj in range(len(list)):
                                        with open(f"{name}.json", "r") as cin1:
                                            aa1 = json.load(cin1)
                                        for jj in aa1:
                                            pat = {"status": jj["status"], "watches": jj["watches"],
                                                   "likes": jj["likes"], "chel": jj["chel"], "chan": jj["chan"]}
                                            pat1 = {"status": jj["status"], "watches": jj["watches"] + storyy,
                                                    "likes": jj["likes"], "chel": jj["chel"], "chan": jj["chan"]}
                                        aa1.remove(pat)
                                        aa1.append(pat1)
                                        with open(f"{name}.json", "w") as cout1:
                                            json.dump(aa1, cout1, ensure_ascii=False)
                                        generate()
                                        if pagee == "pan_static":
                                            page.clean()
                                            page.add(*pan_static)
                                        page.update()

                                else:
                                    for re in result.stories.stories:
                                        with open(f"{name}.json", "r") as cin1:
                                            aa1 = json.load(cin1)
                                        for jj in aa1:
                                            pat = {"status": jj["status"], "watches": jj["watches"],
                                                   "likes": jj["likes"], "chel": jj["chel"], "chan": jj["chan"]}
                                            pat1 = {"status": jj["status"], "watches": jj["watches"] + 1,
                                                    "likes": jj["likes"], "chel": jj["chel"], "chan": jj["chan"]}
                                        aa1.remove(pat)
                                        aa1.append(pat1)
                                        with open(f"{name}.json", "w") as cout1:
                                            json.dump(aa1, cout1, ensure_ascii=False)
                                        generate()
                                        if pagee == "pan_static":
                                            page.clean()
                                            page.add(*pan_static)
                                        page.update()

                                # list.clear()
                                # list1.clear()

                        else:
                            print("Историй нет")
                    except:
                        continue
            except:
                continue
        f.close()
        print("Right")
        client.disconnect()
        with open(f"{name}.json", "r") as din:
            status = json.load(din)
        for j in status:
            pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                       "chan": j["chan"]}
            pattern1 = {"status": "offline", "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                        "chan": j["chan"]}
        status.remove(pattern)
        status.append(pattern1)
        with open(f"{name}.json", "w") as kin:
            json.dump(status, kin, ensure_ascii=False)
        generate()
        if pagee == "pan_static":
            page.clean()
            page.add(*pan_static)
        page.update()

    def start2():
        global a2
        if tim.value.isdigit():

            textt = tim.value
            print(int(textt))
        else:
            list2 = tim.value.split("-")
            textt = random.randint(int(list2[0]), int(list2[-1]))
        print(int(textt))
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("AAA")
        a = []
        text = f"{d.value}"
        with open("base.json", "r") as cin:
            a = json.load(cin)

        try:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
                    zero = j["zero"]
                    one = j["one"]
                    two = j["two"]
                    three = j["three"]
            client = TelegramClient(name, apiid, apihash,
                                    proxy=(python_socks.ProxyType.HTTP, zero, one, True, two, three))
        except:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
            client = TelegramClient(name, apiid, apihash)

        client.connect()

        f = open(f"{sel3}", "r")
        txt = f.read().splitlines()
        print(txt)
        chan = 0
        list = []
        list1 = []
        for rt in txt:
            try:
                chan += 1
                channel = client.get_entity(rt)
                all_participants = client.get_participants(channel)

                status = []

                with open(f"{name}.json", "r") as din:
                    status = json.load(din)
                for j in status:
                    pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                               "chan": j["chan"]}
                    pattern1 = {"status": "Идет парсинг", "watches": j["watches"], "likes": j["likes"],
                                "chel": j["chel"], "chan": j["chan"]}
                status.remove(pattern)
                status.append(pattern1)
                with open(f"{name}.json", "w") as kin:
                    json.dump(status, kin, ensure_ascii=False)
                generate()
                if pagee == "pan_static":
                    page.clean()
                    page.add(*pan_static)
                page.update()
                list = []
                list1 = []

                flog = 0
                for i in range(int(stor.value)):
                    flog += 1

                    list.append(flog)
                print(list)
                print(list[-1])
                chel = 0
                liker = 0
                storyy = 0
                for i in all_participants:
                    try:
                        time.sleep(int(tim.value))
                        if name == a2:
                            print("Right")
                            client.disconnect()
                            with open(f"{name}.json", "r") as din:
                                status = json.load(din)
                            for j in status:
                                pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"],
                                           "chel": j["chel"], "chan": j["chan"]}
                                pattern1 = {"status": "offline", "watches": j["watches"], "likes": j["likes"],
                                            "chel": j["chel"], "chan": j["chan"]}
                            status.remove(pattern)
                            status.append(pattern1)
                            with open(f"{name}.json", "w") as kin:
                                json.dump(status, kin, ensure_ascii=False)
                            generate()
                            if pagee == "pan_static":
                                page.clean()
                                page.add(*pan_static)
                            page.update()
                            return
                        if (
                                not i.stories_unavailable and
                                not i.stories_hidden and
                                i.stories_max_id
                        ):

                            res = client(
                                functions.stories.ReadStoriesRequest(
                                    peer=i.id,
                                    max_id=i.stories_max_id
                                ))
                            if i.username == None:
                                pass
                            else:
                                print(i.username)

                                result = client(functions.stories.GetPeerStoriesRequest(
                                    peer=f'@{i.username}'
                                ))
                                fl = 0
                                fla = 0

                                for re in result.stories.stories:
                                    fl += 1

                                    if fl >= list[-1]:
                                        fla += 1
                                if fla > 0:
                                    storyy = 0
                                    for re in result.stories.stories:
                                        storyy += 1
                                        print(re.id)
                                        list1.append(re.id)

                                    random.shuffle(list)
                                    for jj in range(len(list)):
                                        with open(f"{name}.json", "r") as cin1:
                                            aa1 = json.load(cin1)
                                        for jj in aa1:
                                            pat = {"status": jj["status"], "watches": jj["watches"],
                                                   "likes": jj["likes"], "chel": jj["chel"], "chan": jj["chan"]}
                                            pat1 = {"status": jj["status"], "watches": jj["watches"] + storyy,
                                                    "likes": jj["likes"] + 1, "chel": jj["chel"], "chan": jj["chan"]}
                                        aa1.remove(pat)
                                        aa1.append(pat1)
                                        with open(f"{name}.json", "w") as cout1:
                                            json.dump(aa1, cout1, ensure_ascii=False)
                                        generate()
                                        if pagee == "pan_static":
                                            page.clean()
                                            page.add(*pan_static)
                                        page.update()
                                        result1 = client(functions.stories.SendReactionRequest(
                                            peer=f'@{i.username}',
                                            story_id=random.choice(list1),
                                            reaction=types.ReactionEmoji(
                                                emoticon='💋'
                                            ),
                                            add_to_recent=True
                                        ))
                                        print(result1)
                                        print(random.choice(list1))
                                else:
                                    for re in result.stories.stories:
                                        with open(f"{name}.json", "r") as cin1:
                                            aa1 = json.load(cin1)
                                        for jj in aa1:
                                            pat = {"status": jj["status"], "watches": jj["watches"],
                                                   "likes": jj["likes"], "chel": jj["chel"], "chan": jj["chan"]}
                                            pat1 = {"status": jj["status"], "watches": jj["watches"] + 1,
                                                    "likes": jj["likes"] + 1, "chel": jj["chel"], "chan": jj["chan"]}
                                        aa1.remove(pat)
                                        aa1.append(pat1)
                                        with open(f"{name}.json", "w") as cout1:
                                            json.dump(aa1, cout1, ensure_ascii=False)
                                        generate()
                                        if pagee == "pan_static":
                                            page.clean()
                                            page.add(*pan_static)
                                        page.update()
                                        result1 = client(functions.stories.SendReactionRequest(
                                            peer=f'@{i.username}',
                                            story_id=re.id,
                                            reaction=types.ReactionEmoji(
                                                emoticon='💋'
                                            ),
                                            add_to_recent=True
                                        ))
                                    print(result1)
                                    print(random.choice(list1))
                                # list.clear()
                                # list1.clear()

                        else:
                            print("Историй нет")
                    except:
                        continue
            except:
                continue
        f.close()
        print("Right")
        client.disconnect()
        with open(f"{name}.json", "r") as din:
            status = json.load(din)
        for j in status:
            pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                       "chan": j["chan"]}
            pattern1 = {"status": "offline", "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                        "chan": j["chan"]}
        status.remove(pattern)
        status.append(pattern1)
        with open(f"{name}.json", "w") as kin:
            json.dump(status, kin, ensure_ascii=False)
        generate()
        if pagee == "pan_static":
            page.clean()
            page.add(*pan_static)
        page.update()

    def start1():
        global a1

        if tim.value.isdigit():

            textt = tim.value
            print(int(textt))
        else:
            list2 = tim.value.split("-")
            textt = random.randint(int(list2[0]), int(list2[-1]))
        print(int(textt))
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("AAA")
        a = []
        text = f"{d.value}"
        with open("base.json", "r") as cin:
            a = json.load(cin)

        try:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
                    zero = j["zero"]
                    one = j["one"]
                    two = j["two"]
                    three = j["three"]
            client = TelegramClient(name, apiid, apihash,
                                    proxy=(python_socks.ProxyType.HTTP, zero, one, True, two, three))
        except:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
            client = TelegramClient(name, apiid, apihash)

        client.connect()
        f = open(f"{sel2}", "r")
        filee = f.read().splitlines()
        f.close()

        status = []
        generate()
        with open(f"{name}.json", "r") as din:
            status = json.load(din)
        for j in status:
            pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                       "chan": j["chan"]}
            pattern1 = {"status": "Идет рассылка", "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                        "chan": j["chan"]}
        status.remove(pattern)
        status.append(pattern1)
        with open(f"{name}.json", "w") as kin:
            json.dump(status, kin, ensure_ascii=False)
        generate()
        if pagee == "pan_static":
            page.clean()
            page.add(*pan_static)
        page.update()
        list = []
        list1 = []

        flog = 0
        for i in range(int(stor.value)):
            flog += 1

            list.append(flog)
        print(list)
        print(list[-1])
        chel = 0
        liker = 0
        storyy = 0
        for i in filee:
            try:
                if a1 == name:
                    a1 = "none"
                    with open(f"{name}.json", "r") as cin1:
                        aa1 = json.load(cin1)
                    for jj in aa1:
                        pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                               "chel": jj["chel"], "chan": jj["chan"]}
                        pat1 = {"status": "offline", "watches": jj["watches"], "likes": jj["likes"], "chel": jj["chel"],
                                "chan": jj["chan"]}
                    aa1.remove(pat)
                    aa1.append(pat1)
                    with open(f"{name}.json", "w") as cout1:
                        json.dump(aa1, cout1, ensure_ascii=False)
                    generate()
                    if pagee == "pan_static":
                        page.clean()
                        page.add(*pan_static)
                    page.update()

                    print("Right")
                    client.disconnect()
                    return

                time.sleep(0.1)
                time.sleep(int(textt))
                print(i)
                print(chel)

                result = client(functions.stories.GetPeerStoriesRequest(
                    peer=f'@{i}'
                ))
                fl = 0
                fla = 0

                for re in result.stories.stories:
                    fl += 1
                    print(fl)

                    if fl >= list[-1]:
                        fla += 1
                if fla > 0:
                    storyy = 0
                    for re in result.stories.stories:
                        storyy += 1
                        print(re.id)
                        list1.append(re.id)

                    random.shuffle(list)
                    for jj in range(len(list)):
                        with open(f"{name}.json", "r") as cin1:
                            aa1 = json.load(cin1)
                        for jj in aa1:
                            pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                                   "chel": jj["chel"], "chan": jj["chan"]}
                            pat1 = {"status": jj["status"], "watches": jj["watches"] + storyy, "likes": jj["likes"] + 1,
                                    "chel": jj["chel"], "chan": jj["chan"]}
                        aa1.remove(pat)
                        aa1.append(pat1)
                        with open(f"{name}.json", "w") as cout1:
                            json.dump(aa1, cout1, ensure_ascii=False)
                        generate()
                        if pagee == "pan_static":
                            page.clean()
                            page.add(*pan_static)
                        page.update()
                        result1 = client(functions.stories.SendReactionRequest(
                            peer=f'@{i}',
                            story_id=random.choice(list1),
                            reaction=types.ReactionEmoji(
                                emoticon='💋'
                            ),
                            add_to_recent=True
                        ))
                        print(result1)
                        print(random.choice(list1))
                else:
                    for re in result.stories.stories:
                        with open(f"{name}.json", "r") as cin1:
                            aa1 = json.load(cin1)
                        for jj in aa1:
                            pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                                   "chel": jj["chel"], "chan": jj["chan"]}
                            pat1 = {"status": jj["status"], "watches": jj["watches"] + 1, "likes": jj["likes"] + 1,
                                    "chel": jj["chel"], "chan": jj["chan"]}
                        aa1.remove(pat)
                        aa1.append(pat1)
                        with open(f"{name}.json", "w") as cout1:
                            json.dump(aa1, cout1, ensure_ascii=False)
                        generate()
                        if pagee == "pan_static":
                            page.clean()
                            page.add(*pan_static)
                        page.update()
                        result1 = client(functions.stories.SendReactionRequest(
                            peer=f'@{i.username}',
                            story_id=re.id,
                            reaction=types.ReactionEmoji(
                                emoticon='💋'
                            ),
                            add_to_recent=True
                        ))
                    print(result1)
                    print(random.choice(list1))








            except:
                continue
        aa1 = []
        with open(f"{name}.json", "r") as cin1:
            aa1 = json.load(cin1)
        for jj in aa1:
            pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"], "chel": jj["chel"],
                   "chan": jj["chan"]}
            pat1 = {"status": "offline", "watches": jj["watches"], "likes": jj["likes"], "chel": jj["chel"],
                    "chan": jj["chan"]}
        aa1.remove(pat)
        aa1.append(pat1)
        with open(f"{name}.json", "w") as cout1:
            json.dump(aa1, cout1, ensure_ascii=False)
        f.close()
        generate()
        if pagee == "pan_static":
            page.clean()
            page.add(*pan_static)
        page.update()

        print("Right")
        client.disconnect()

    def start4():
        global a1

        if tim.value.isdigit():

            textt = tim.value
            print(int(textt))
        else:
            list2 = tim.value.split("-")
            textt = random.randint(int(list2[0]), int(list2[-1]))
        print(int(textt))
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("AAA")
        a = []
        text = f"{d.value}"
        with open("base.json", "r") as cin:
            a = json.load(cin)

        try:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
                    zero = j["zero"]
                    one = j["one"]
                    two = j["two"]
                    three = j["three"]
            client = TelegramClient(name, apiid, apihash,
                                    proxy=(python_socks.ProxyType.HTTP, zero, one, True, two, three))
        except:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
            client = TelegramClient(name, apiid, apihash)

        client.connect()
        f = open(f"{sel2}", "r")
        filee = f.read().splitlines()
        f.close()

        status = []
        generate()
        with open(f"{name}.json", "r") as din:
            status = json.load(din)
        for j in status:
            pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                       "chan": j["chan"]}
            pattern1 = {"status": "Идет рассылка", "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                        "chan": j["chan"]}
        status.remove(pattern)
        status.append(pattern1)
        with open(f"{name}.json", "w") as kin:
            json.dump(status, kin, ensure_ascii=False)
        generate()
        if pagee == "pan_static":
            page.clean()
            page.add(*pan_static)
        page.update()
        list = []
        list1 = []

        flog = 0
        for i in range(int(stor.value)):
            flog += 1

            list.append(flog)
        print(list)
        print(list[-1])
        chel = 0
        liker = 0
        storyy = 0
        for i in filee:
            try:
                if a1 == name:
                    a1 = "none"
                    with open(f"{name}.json", "r") as cin1:
                        aa1 = json.load(cin1)
                    for jj in aa1:
                        pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                               "chel": jj["chel"], "chan": jj["chan"]}
                        pat1 = {"status": "offline", "watches": jj["watches"], "likes": jj["likes"], "chel": jj["chel"],
                                "chan": jj["chan"]}
                    aa1.remove(pat)
                    aa1.append(pat1)
                    with open(f"{name}.json", "w") as cout1:
                        json.dump(aa1, cout1, ensure_ascii=False)
                    generate()
                    if pagee == "pan_static":
                        page.clean()
                        page.add(*pan_static)
                    page.update()

                    print("Right")
                    client.disconnect()
                    return

                time.sleep(0.1)
                time.sleep(int(textt))
                print(i)
                print(chel)

                result = client(functions.stories.GetPeerStoriesRequest(
                    peer=f'@{i}'
                ))
                fl = 0
                fla = 0

                for re in result.stories.stories:
                    fl += 1
                    print(fl)

                    if fl >= list[-1]:
                        fla += 1
                if fla > 0:
                    storyy = 0
                    for re in result.stories.stories:
                        storyy += 1
                        print(re.id)
                        list1.append(re.id)

                    random.shuffle(list)
                    for jj in range(len(list)):
                        with open(f"{name}.json", "r") as cin1:
                            aa1 = json.load(cin1)
                        for jj in aa1:
                            pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                                   "chel": jj["chel"], "chan": jj["chan"]}
                            pat1 = {"status": jj["status"], "watches": jj["watches"] + storyy, "likes": jj["likes"] + 1,
                                    "chel": jj["chel"], "chan": jj["chan"]}
                        aa1.remove(pat)
                        aa1.append(pat1)
                        with open(f"{name}.json", "w") as cout1:
                            json.dump(aa1, cout1, ensure_ascii=False)
                        generate()
                        if pagee == "pan_static":
                            page.clean()
                            page.add(*pan_static)
                        page.update()

                else:
                    for re in result.stories.stories:
                        with open(f"{name}.json", "r") as cin1:
                            aa1 = json.load(cin1)
                        for jj in aa1:
                            pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                                   "chel": jj["chel"], "chan": jj["chan"]}
                            pat1 = {"status": jj["status"], "watches": jj["watches"] + 1, "likes": jj["likes"] + 1,
                                    "chel": jj["chel"], "chan": jj["chan"]}
                        aa1.remove(pat)
                        aa1.append(pat1)
                        with open(f"{name}.json", "w") as cout1:
                            json.dump(aa1, cout1, ensure_ascii=False)
                        generate()
                        if pagee == "pan_static":
                            page.clean()
                            page.add(*pan_static)
                        page.update()









            except:
                continue
        aa1 = []
        with open(f"{name}.json", "r") as cin1:
            aa1 = json.load(cin1)
        for jj in aa1:
            pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"], "chel": jj["chel"],
                   "chan": jj["chan"]}
            pat1 = {"status": "offline", "watches": jj["watches"], "likes": jj["likes"], "chel": jj["chel"],
                    "chan": jj["chan"]}
        aa1.remove(pat)
        aa1.append(pat1)
        with open(f"{name}.json", "w") as cout1:
            json.dump(aa1, cout1, ensure_ascii=False)
        f.close()
        generate()
        if pagee == "pan_static":
            page.clean()
            page.add(*pan_static)
        page.update()

        print("Right")
        client.disconnect()

    def start():
        global name_stop

        f1 = open(f"{sel1}", "r+")
        par = f1.read().splitlines()
        print(par)
        f1.close()

        loop1 = asyncio.new_event_loop()
        asyncio.set_event_loop(loop1)

        a = []
        text = f"{d.value}"
        with open("base.json", "r") as cin:
            a = json.load(cin)

        try:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
                    zero = j["zero"]
                    one = j["one"]
                    two = j["two"]
                    three = j["three"]
                client = TelegramClient(name, apiid, apihash,
                                        proxy=(python_socks.ProxyType.HTTP, zero, one, True, two, three))
        except:
            for j in a:
                if j["name"] == text:
                    name = j["name"]
                    apiid = j["api_id"]
                    apihash = j["api_hash"]
            client = TelegramClient(name, apiid, apihash)

        client.connect()
        list = []
        list1 = []

        f = open(f"{sel}", "r")

        txt = f.read().splitlines()
        print(txt)
        chan = 0
        for rt in txt:
            try:
                chan += 1
                channel = client.get_entity(rt)
                all_participants = client.get_participants(channel)

                status = []

                with open(f"{name}.json", "r") as din:
                    status = json.load(din)
                for j in status:
                    pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                               "chan": j["chan"]}
                    pattern1 = {"status": "Идет парсинг", "watches": j["watches"], "likes": j["likes"],
                                "chel": j["chel"], "chan": j["chan"] + 1}
                status.remove(pattern)
                status.append(pattern1)
                with open(f"{name}.json", "w") as kin:
                    json.dump(status, kin, ensure_ascii=False)
                generate()
                if pagee == "pan_static":
                    page.clean()
                    page.add(*pan_static)
                page.update()
                hui = 0
                chel = 0
                liker = 0
                storyy = 0
                kklag = 0
                for i in all_participants:
                    try:
                        time.sleep(int(tim.value))
                        if name == name_stop:
                            print("Right")
                            client.disconnect()
                            with open(f"{name}.json", "r") as din:
                                status = json.load(din)
                            for j in status:
                                pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"],
                                           "chel": j["chel"], "chan": j["chan"]}
                                pattern1 = {"status": "offline", "watches": j["watches"], "likes": j["likes"],
                                            "chel": j["chel"], "chan": j["chan"]}
                            status.remove(pattern)
                            status.append(pattern1)
                            with open(f"{name}.json", "w") as kin:
                                json.dump(status, kin, ensure_ascii=False)
                            generate()
                            if pagee == "pan_static":
                                page.clean()
                                page.add(*pan_static)
                            page.update()
                            return
                        if (
                                not i.stories_unavailable and
                                not i.stories_hidden and
                                i.stories_max_id
                        ):
                            chel += 1

                            res = client(
                                functions.stories.ReadStoriesRequest(
                                    peer=i.id,
                                    max_id=i.stories_max_id
                                ))
                            if i.username == None:
                                pass
                            else:

                                if i.username in par:
                                    print("FFF")
                                else:
                                    print("ASDASDASD")
                                    f1 = open(f"{sel1}", "a")
                                    f1.write(f"{i.username}\n")
                                    with open(f"{name}.json", "r") as cin1:
                                        aa1 = json.load(cin1)
                                    for jj in aa1:
                                        pat = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                                               "chel": jj["chel"], "chan": jj["chan"]}
                                        pat1 = {"status": jj["status"], "watches": jj["watches"], "likes": jj["likes"],
                                                "chel": jj["chel"] + 1, "chan": jj["chan"]}
                                    aa1.remove(pat)
                                    aa1.append(pat1)
                                    with open(f"{name}.json", "w") as cout1:
                                        json.dump(aa1, cout1, ensure_ascii=False)
                                    f1.close()
                                    generate()
                                    if pagee == "pan_static":
                                        page.clean()
                                        page.add(*pan_static)
                                    page.update()

                                print(i.username)
                                print(hui)
                                # list.clear()
                                # list1.clear()

                        else:
                            print("Историй нет")



                    except:
                        continue
            except:
                continue

        f.close()
        print("Right")
        client.disconnect()
        with open(f"{name}.json", "r") as din:
            status = json.load(din)
        for j in status:
            pattern = {"status": j["status"], "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                       "chan": j["chan"]}
            pattern1 = {"status": "offline", "watches": j["watches"], "likes": j["likes"], "chel": j["chel"],
                        "chan": j["chan"]}
        status.remove(pattern)
        status.append(pattern1)
        with open(f"{name}.json", "w") as kin:
            json.dump(status, kin, ensure_ascii=False)
        generate()
        if pagee == "pan_static":
            page.clean()
            page.add(*pan_static)
        page.update()

    def auth(e):

        try:
            loop3 = asyncio.new_event_loop()
            asyncio.set_event_loop(loop3)
            if proxy.value == "":
                client = TelegramClient(name.value, apiid.value, apihash.value)
            else:
                client = TelegramClient(name.value, apiid.value, apihash.value,
                                        proxy=(python_socks.ProxyType.HTTP, f'{proxy.value.split(":")[0]}',
                                               int(f'{proxy.value.split(":")[1]}'), True,
                                               f'{proxy.value.split(":")[2]}', f'{proxy.value.split(":")[3]}'))

            client.connect()
            dlg_modal = ft.AlertDialog(
                modal=False,
                title=ft.Text("Пожалуйста подтвердите"),
                content=ft.Text("Введите код с тг:"),
                actions=[code, ft.FilledButton(text="Ок", on_click=lambda e, client=client: auth1(e, client))]
            )
            if not client.is_user_authorized():
                client.sign_in(number.value)
                page.open(dlg_modal)

        except Exception as e:
            dlg0 = ft.AlertDialog(
                modal=False,
                title=ft.Text(f"{e}")
            )
            print(e)
            page.open(dlg0)

        def auth1(e, client):
            try:
                try:
                    client.sign_in(number.value, code.value)
                    client.disconnect()
                except telethon.errors.SessionPasswordNeededError:
                    client.sign_in(password=password.value)
                    client.disconnect()
                d.options.append(ft.dropdown.Option(name.value))
                d1.options.append(ft.dropdown.Option(name.value))
                generate()
                a = []
                with open("base.json", "r") as cin:
                    a = json.load(cin)
                if proxy.value == "":
                    a.append({"name": f"{name.value}", "api_id": f"{apiid.value}", "api_hash": f"{apihash.value}",
                              "password": f"{password.value}"})
                else:
                    a.append({"name": f"{name.value}", "api_id": f"{apiid.value}", "api_hash": f"{apihash.value}",
                              "password": f"{password.value}", "zero": f'{proxy.value.split(":")[0]}',
                              "one": int(f'{proxy.value.split(":")[1]}'), "two": f'{proxy.value.split(":")[2]}',
                              "three": f'{proxy.value.split(":")[3]}'})
                with open("base.json", "w") as cout:
                    json.dump(a, cout, ensure_ascii=False)
                proxy.value = ""
                name.value = ""
                number.value = ""
                password.value = ""
                apiid.value = ""
                apihash.value = ""
                code.value = ""
                page.close(dlg_modal)
                page.update()
                page.add(*pan_auth)
                page.update()
            except Exception as e:
                dlg0 = ft.AlertDialog(
                    modal=False,
                    title=ft.Text(f"{e}")
                )
                print(e)
                print(traceback.format_exc())
                page.open(dlg0)

    def del1(e):
        if d1.value == "" and d.value == "":
            pass
        else:
            option = find_option(d1.value)

            option1 = find_option1(d1.value)

            if option != None:
                d1.options.remove(option)

                os.remove(f"{d1.value}.json")
                os.remove(f"{d1.value}.session")

            if option1 != None:
                d.options.remove(option1)

            a = []
            with open("base.json", "r") as cin:
                a = json.load(cin)
            flag = 0
            for i in a:
                if i["name"] == f"{d1.value}":
                    flag += 1
                    try:
                        pattern2 = {"name": i["name"], "api_id": i["api_id"], "api_hash": i["api_hash"],
                                    "password": i["password"], "zero": i["zero"], "one": i["one"], "two": i["two"],
                                    "three": i["three"]}
                    except:
                        pattern1 = {"name": i["name"], "api_id": i["api_id"], "api_hash": i["api_hash"],
                                    "password": i["password"]}
            if flag > 0:
                try:
                    a.remove(pattern1)
                except:
                    a.remove(pattern2)
            with open("base.json", "w") as cout:
                json.dump(a, cout, ensure_ascii=False)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.PERSON_ADD_ALT_1_SHARP, label="Авторизация"),
            ft.NavigationBarDestination(icon=ft.Icons.NOT_STARTED, label="Авторизованные аккаунты"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER, label="Статистика", ),
        ], on_change=navigate
    )

    proxy = ft.TextField(label="Прокси", autofocus=True)
    name = ft.TextField(label="Имя аккаунта", autofocus=True)
    number = ft.TextField(label="Номер телефона", autofocus=True)
    password = ft.TextField(label="Пароль", autofocus=True)
    apihash = ft.TextField(label="Api hash", autofocus=True)
    apiid = ft.TextField(label="Api id", autofocus=True)
    button_auth = ft.FilledButton(text="Авторизовать аккаунт", on_click=auth)
    button_start = ft.FilledButton(text="Начать парсинг", on_click=go)

    button_startparse = ft.FilledButton(text="Начать парсинг, просмотры и лайки историй", on_click=GO)
    button_startparse1 = ft.FilledButton(text="Начать парсинг и просмотры историй", on_click=GO1)

    code = ft.TextField(label="Code", autofocus=True)
    # url = ft.TextField(label = "Ссылка", autofocus=True)
    llll = ft.TextField(label="Сколько историй смотреть у одного пользователя", autofocus=True)
    stor = ft.TextField(label="Сколько историй лайкать у одного пользователя", autofocus=True)
    tim = ft.TextField(label="Задержка", autofocus=True)
    but_start = ft.FilledButton(text="Начать просмотры и лайки историй", on_click=parse)
    but_start1 = ft.FilledButton(text="Начать просмотры историй", on_click=parse1)
    but_stop = ft.FilledButton(text="Закончить рассылку", on_click=stoparse)

    but_delete = ft.FilledButton(text="Удалить аккаунт", on_click=del1)
    page.overlay.extend([pick_files_dialog1, pick_files_dialog2, pick_files_dialog3, pick_files_dialog4])

    pan_auth = (proxy, name, number, password, apihash, apiid, button_auth, d1, but_delete)
    pan_work = (d, button_pick, button_add, button_select, button_pick1, llll, stor, tim, button_start, but_start,
                but_start1, button_startparse, button_startparse1)

    page.add(*pan_auth)


ft.app(target=main)
