[authorization-code-with-pkce.html](https://www.oauth.com/playground/authorization-code-with-pkce.html)

```html

<pre class="auth-url-string"><span class="okta-url"></span>/authorize?<span class="auth-params">
  response_type=code
  &amp;client_id=<span class="client-id"></span>
  &amp;redirect_uri=<span class="base-url"></span>/authorization-code-with-pkce.html
  &amp;scope=photo+offline_access
  &amp;state=<span class="oauth2-state"></span>
  &amp;code_challenge=<span class="code-challenge"></span>
  &amp;code_challenge_method=S256</span></pre>

<footer class="card-footer">
    <div class="card-footer-item"><a href="#" class="button is-primary auth-url">Authorize</a></div>
</footer>
```

```js
$(".auth-url").click(function(){
    window.location = Cookies.get("base_url")+"/auth-dialog.html?"+$(".auth-url-string .auth-params").text().replace(/\s/g,"");
    return false;
});
```

```js
https://www.oauth.com/playground/auth-dialog.html?
response_type=code
&client_id=82vCV9LRCK_NU_TNqH-L0ZEU
&redirect_uri=https://www.oauth.com/playground/authorization-code-with-pkce.html
&scope=photo+offline_access&state=OUKC8fU1ESq608m6
&code_challenge=WUbgQSSsOTPZFSteIVw4apxfJQGpEAOXZFj7fAonZeU
&code_challenge_method=S256
```
