## AWS Multi-Account Login Portal Without SSO 🚀

This project provides secure and seamless access to multiple AWS accounts without using any third-party SSO tools. Instead, it leverages IAM role switching and AWS STS AssumeRole to authenticate users dynamically across AWS environments.

_🔍 Why Not Use an SSO Tool?_

Many organizations rely on SSO tools like AWS IAM Identity Center (formerly AWS SSO), Okta, or OneLogin for AWS account access. However, these tools come with limitations: 

✅ Requires additional setup & maintenance

✅ May not work well for all AWS accounts & environments

✅ Tied to corporate authentication systems

✅ Might not be allowed in highly regulated environments

_💡 Alternative Approach: AWS IAM Role Switching_

Instead of an SSO tool, this project achieves the same functionality by:

Using IAM roles to provide access to multiple AWS accounts

Dynamically generating AWS Console login URLs

Using AWS STS (Security Token Service) AssumeRole to get temporary credentials

Allowing seamless account switching via a web portal

_🚀 Solution Overview_

- User selects an AWS account from a dropdown.

- Flask application assumes the correct IAM role for that account.

- AWS STS returns short-lived session credentials.

- A sign-in URL is generated for the AWS Console using these credentials.

- User is automatically redirected to the AWS Console, without manually entering credentials.

✅ No SSO integration required

✅ No need to manage multiple AWS access keys

✅ Works across multiple AWS accounts dynamically

_📌 How This Implementation Works_

- Uses a single IAM user to assume roles in multiple AWS accounts.

- IAM roles are pre-configured in each AWS account.

- Trust relationships allow cross-account access.

- No third-party authentication required, everything is handled within AWS.

_Why This Approach is Better?_

✅ No SSO tool required

✅ Secure authentication with IAM roles

✅ No need to share AWS credentials

✅ Fully automated and scalable

_🌟 Conclusion_

This solution provides secure, scalable AWS multi-account access without relying on any third-party SSO tools. If you're looking for an alternative to AWS SSO, Okta, or other identity providers, this approach can achieve similar functionality while keeping everything within AWS IAM.
