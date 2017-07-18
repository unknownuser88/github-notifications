Github Notifications
================

This plugin show github notifications count in statusbar

## Generating Access Token

* Account Settings -> [Personal access tokens](https://github.com/settings/tokens)
* "Generate new token" under "Personal access tokens"
* For "Token description" you should give it a meaningful name, Example: sublime notifications plugin
* Under "Select scopes" you can just select notifications

Paste the token in the settings section under the token option.

## Settings

```javascript
{
    "token": "", // Your GitHub API token
    "update_interval": 60, // seconds
    "template": "Github: {notif}"
}

```

## Commands

```javascript
{
    "caption": "Open Github Notifications",
    "command": "open_github_notifications"
}
```

## Screenshot

![Screenshot](https://github.com/unknownuser88/github-notifications/raw/master/github-notifications.png)
