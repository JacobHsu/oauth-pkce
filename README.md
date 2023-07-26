# oauth-pkce

[OAuth 2.0 Playground](https://www.oauth.com/playground/) > [PKCE](https://www.oauth.com/playground/authorization-code-with-pkce.html)  

<<<<<<< HEAD
Client Registration `login` / `password`  open in new window  


> https://www.oauth.com/playground/auth-dialog.html?response_type=code&client_id=ZZCIUL40CpIZc4Mr_UUqdVCK&redirect_uri=https://www.oauth.com/playground/authorization-code-with-pkce.html&scope=photo+offline_access&state=KBlwFJSXABVJ0FPC&code_challenge=y0GgBbtf-sLVpWqmvvOTGdXt1SN_For8Z75YVhUfvKU&code_challenge_method=S256

```
https://authorization-server.com/authorize?
  response_type=code
  &client_id=ZZCIUL40CpIZc4Mr_UUqdVCK
  &redirect_uri=https://www.oauth.com/playground/authorization-code-with-pkce.html
  &scope=photo+offline_access
  &state=sMXJoNorcFdHLdvK
  &code_challenge=uGT6mumN_HrB_SVDgikqZRqKb3L2AMoootTCDXgh5HY
  &code_challenge_method=S256
```

3. Verify the state parameter

/auth-dialog.html?redirect_uri=xxx  
`$("#redirect-uri").attr("href", params.get('redirect_uri')+"?state="+params.get('state')+"&code="+code);`

```
https://www.oauth.com/playground/authorization-code-with-pkce.html?
state=zVf5Qi2m-VSByNOZ
&code=TtQTS9m4upOZ5aBFMw0HjW0DKAKwmbA3byxpGIys4OW_VuAw
```

```js
function generate_auth_code() {
  return random_string(48);
}
```

## js-cookie

打開 Chrome 瀏覽器並導航到你設定 cookie 的網站。
點選右上角的菜單按鈕（三個豎點）並選擇 "更多工具"。
在下拉菜單中選擇 "開發者工具"。
在彈出的開發者工具窗口中，選擇 "Application" 選項卡。
在左側的導覽列中，選擇 "Storage" > "Cookies"。
在右側的窗格中，你將看到所有與當前網站相關的 cookie。選擇你想查看的 cookie，其中將包括你使用 Cookies.set() 方法設定的 cookie。

`if((Cookies.get("user_login") != $("#username").val() || Cookies.get("user_password") != $("#password").val())) {`

Cookies.get("user_login") Cookies / www.oauth.com / `user_login`
Cookies.get("user_password")  Cookies / www.oauth.com / `user_password`

## gh-pages

`git branch  gh-pages`  
`git checkout gh-pages`  
`git push origin gh-pages`
=======
> https://www.oauth.com/playground/auth-dialog.html?response_type=code&client_id=ZZCIUL40CpIZc4Mr_UUqdVCK&redirect_uri=https://www.oauth.com/playground/authorization-code-with-pkce.html&scope=photo+offline_access&state=KBlwFJSXABVJ0FPC&code_challenge=y0GgBbtf-sLVpWqmvvOTGdXt1SN_For8Z75YVhUfvKU&code_challenge_method=S256


會員授權  
1.	引導用戶授權伺服器，發起授權請求 `clientId+redirectUri+state+code_challenge`
2.	用戶登入並同意授權 
3.	返回State & 授權碼Code (有時效性) 
4.	透過授權code換取Access Token `clientId+ client_secrect+redirectUri+code+code_verifier`
5.	返回Access Token (有時效性) 
>>>>>>> 6b33a3403730bd486a3b73439feb8acd3e3251be
