# oauth-pkce

[OAuth 2.0 Playground](https://www.oauth.com/playground/) > [PKCE](https://www.oauth.com/playground/authorization-code-with-pkce.html)  

> https://www.oauth.com/playground/auth-dialog.html?response_type=code&client_id=ZZCIUL40CpIZc4Mr_UUqdVCK&redirect_uri=https://www.oauth.com/playground/authorization-code-with-pkce.html&scope=photo+offline_access&state=KBlwFJSXABVJ0FPC&code_challenge=y0GgBbtf-sLVpWqmvvOTGdXt1SN_For8Z75YVhUfvKU&code_challenge_method=S256


會員授權  
1.	引導用戶授權伺服器，發起授權請求 `clientId+redirectUri+state+code_challenge`
2.	用戶登入並同意授權 
3.	返回State & 授權碼Code (有時效性) 
4.	透過授權code換取Access Token `clientId+ client_secrect+redirectUri+code+code_verifier`
5.	返回Access Token (有時效性) 
