### Installation

#### Sign up for Auth0 account

If you haven't already done so, [sign up](https://auth0.com/signup) for your free Auth0 account and create an application in the dashboard. Find the **domain** and **client ID** from your app settings, as these will be required to integrate Auth0 in your Chrome extension.

#### Install the extension as unpacked extension in Chrome

You will need to do this to get the app id from chrome extension manager. The extension won't work at this stage. But we need the ID anyway. It will be something like "ghbmnnjooekpmoecnnnilnnbdlolhkhi". Keep this handy

_This will change when we actually publish it to Chrome Store_

#### Whitelist Callback URL

In the **Allowed Callback URLs** section, whitelist your callback URL.

```bash
https://<YOUR_APP_ID>.chromiumapp.org/auth0
```

In the **Allowed Logout URLs** section, whitelist your logout URL.

```bash
https://<YOUR_APP_ID>.chromiumapp.org/auth0
```

In the **Allowed Origins** section, whitelist your chrome extension as an origin.

```bash
chrome-extension://<YOUR_APP_ID>
```

#### Add your Application Keys

In `env.js` and provide your Auth0 credentials.

```js
window.env = {
AUTH0_DOMAIN: 'YOUR_AUTH0_DOMAIN',
AUTH0_CLIENT_ID: 'YOUR_AUTH0_CLIENT_ID',
};
```
