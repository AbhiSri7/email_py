import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from smtplib import SMTPAuthenticationError, SMTPRecipientsRefused
import pandas as pd


mail_content = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
        <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width">
        <!--[if !mso]><!-->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!--<![endif]-->
        <title></title>
        <!--[if !mso]><!-->
        <link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet" type="text/css">
        <!--<![endif]-->
        <style type="text/css">
                body {
                        margin: 0;
                        padding: 0;
                }

                table,
                td,
                tr {
                        vertical-align: top;
                        border-collapse: collapse;
                }

                * {
                        line-height: inherit;
                }

                a[x-apple-data-detectors=true] {
                        color: inherit !important;
                        text-decoration: none !important;
                }
        </style>
        <style type="text/css" id="media-query">
                @media (max-width: 520px) {

                        .block-grid,
                        .col {
                                min-width: 320px !important;
                                max-width: 100% !important;
                                display: block !important;
                        }

                        .block-grid {
                                width: 100% !important;
                        }

                        .col {
                                width: 100% !important;
                        }

                        .col>div {
                                margin: 0 auto;
                        }

                        img.fullwidth,
                        img.fullwidthOnMobile {
                                max-width: 100% !important;
                        }

                        .no-stack .col {
                                min-width: 0 !important;
                                display: table-cell !important;
                        }

                        .no-stack.two-up .col {
                                width: 50% !important;
                        }

                        .no-stack .col.num4 {
                                width: 33% !important;
                        }

                        .no-stack .col.num8 {
                                width: 66% !important;
                        }

                        .no-stack .col.num4 {
                                width: 33% !important;
                        }

                        .no-stack .col.num3 {
                                width: 25% !important;
                        }

                        .no-stack .col.num6 {
                                width: 50% !important;
                        }

                        .no-stack .col.num9 {
                                width: 75% !important;
                        }

                        .video-block {
                                max-width: none !important;
                        }

                        .mobile_hide {
                                min-height: 0px;
                                max-height: 0px;
                                max-width: 0px;
                                display: none;
                                overflow: hidden;
                                font-size: 0px;
                        }

                        .desktop_hide {
                                display: block !important;
                                max-height: none !important;
                        }
                }
        </style>
</head>

<body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #f5ecf2;">
        <!--[if IE]><div class="ie-browser"><![endif]-->
        <table class="nl-container" style="table-layout: fixed; vertical-align: top; min-width: 320px; Margin: 0 auto; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f5ecf2; width: 100%;" cellpadding="0" cellspacing="0" role="presentation" width="100%" bgcolor="#f5ecf2" valign="top">
                <tbody>
                        <tr style="vertical-align: top;" valign="top">
                                <td style="word-break: break-word; vertical-align: top;" valign="top">
                                        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#f5ecf2"><![endif]-->
                                        <div style="background-color:transparent;">
                                                <div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                                                <!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                                                <div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
                                                                        <div style="width:100% !important;">
                                                                                <!--[if (!mso)&(!IE)]><!-->
                                                                                <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                                                        <!--<![endif]-->
                                                                                        <div class="img-container center fixedwidth" align="center" style="padding-right: 0px;padding-left: 0px;">
                                                                                                <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img class="center fixedwidth" align="center" border="0" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/583187_564778/editor_images/logoLightBg.png" alt="Alternate text" title="Alternate text" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 100px; display: block;" width="100">
                                                                                                <!--[if mso]></td></tr></table><![endif]-->
                                                                                        </div>
                                                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                                                                <tbody>
                                                                                                        <tr style="vertical-align: top;" valign="top">
                                                                                                                <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #BBBBBB; width: 100%;" align="center" role="presentation" valign="top">
                                                                                                                                <tbody>
                                                                                                                                        <tr style="vertical-align: top;" valign="top">
                                                                                                                                                <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
                                                                                                                                        </tr>
                                                                                                                                </tbody>
                                                                                                                        </table>
                                                                                                                </td>
                                                                                                        </tr>
                                                                                                </tbody>
                                                                                        </table>
                                                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 0px; font-family: Georgia, 'Times New Roman', serif"><![endif]-->
                                                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                                                        <!--[if (!mso)&(!IE)]><!-->
                                                                                </div>
                                                                                <!--<![endif]-->
                                                                        </div>
                                                                </div>
                                                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                                        </div>
                                                </div>
                                        </div>					
                                        <div style="background-color:transparent;">
                                                <div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                                                <!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                                                <div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
                                                                        <div style="width:100% !important;">
                                                                                <!--[if (!mso)&(!IE)]><!-->
                                                                                <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                                                        <!--<![endif]-->
                                                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 0px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                                                        <div style="color:#393d47;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;line-height:1.2;padding-top:0px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                                                                <div style="line-height: 1.2; font-size: 12px; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; color: #393d47; mso-line-height-alt: 14px;">
                                                                                                        <p style="font-size: 17px; line-height: 1.2; word-break: break-word; text-align: justify; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; mso-line-height-alt: 20px; mso-ansi-font-size: 18px; margin: 0;"><span style="font-size: 17px; mso-ansi-font-size: 18px;">Dear Member,<br><br>
                                                                                                                Thank you for your dedication and hard work towards making 2020-2021 a successful year for IEEE SBM. Your Certificate of Appreciation as a Managing Committee member of IEEE SBM has been attached herewith.
                                                                                                                
                                                                                                                We wish you the best for your future endeavours and goals!<br><br>
                                                                                                                Yours Sincerely,
                                                                                                                IEEE SBM</span></em></p>
                                                                                                </div>
                                                                                        </div>
                                                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                                                        <!--[if (!mso)&(!IE)]><!-->
                                                                                </div>
                                                                                <!--<![endif]-->
                                                                        </div>
                                                                </div>
                                                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                                        </div>
                                                </div>
                                        </div>
                                        <div style="background-color:transparent;">
                                                <div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                                                <!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:15px;"><![endif]-->
                                                                <div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
                                                                        <div style="width:100% !important;">
                                                                                <!--[if (!mso)&(!IE)]><!-->
                                                                                <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:15px; padding-right: 0px; padding-left: 0px;">
                                                                                        <!--<![endif]-->
                                                                                        <!--[if (!mso)&(!IE)]><!-->
                                                                                </div>
                                                                                <!--<![endif]-->
                                                                        </div>
                                                                </div>
                                                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                                        </div>
                                                </div>
                                        </div>
                                        <div style="background-color:#25221d;">
                                                <div class="block-grid " style="Margin: 0 auto; min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#25221d;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                                                <!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]-->
                                                                <div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
                                                                        <div style="width:100% !important;">
                                                                                <!--[if (!mso)&(!IE)]><!-->
                                                                                <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;">
                                                                                        <!--<![endif]-->
                                                                                        <table class="social_icons" cellpadding="0" cellspacing="0" width="100%" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top">
                                                                                                <tbody>
                                                                                                        <tr style="vertical-align: top;" valign="top">
                                                                                                                <td style="word-break: break-word; vertical-align: top; padding-top: 10px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top">
                                                                                                                        <table class="social_table" align="center" cellpadding="0" cellspacing="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;" valign="top">
                                                                                                                                <tbody>
                                                                                                                                        <tr style="vertical-align: top; display: inline-block; text-align: center;" align="center" valign="top">
                                                                                                                                                <td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 2.5px; padding-left: 2.5px;" valign="top"><a href="https://www.facebook.com/ieeesbmanipal" target="_blank"><img width="32" height="32" src="https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/facebook@2x.png" alt="Facebook" title="Facebook" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"></a></td>
                                                                                                                                                <td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 2.5px; padding-left: 2.5px;" valign="top"><a href="https://www.instagram.com/ieeesbm/" target="_blank"><img width="32" height="32" src="https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/instagram@2x.png" alt="Instagram" title="Instagram" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"></a></td>
                                                                                                                                                <td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 2.5px; padding-left: 2.5px;" valign="top"><a href="mailto:contactus.ieeesbmanipal.com" target="_blank"><img width="32" height="32" src="https://d2fi4ri5dhpqd1.cloudfront.net/public/resources/social-networks-icon-sets/circle-color/googleplus@2x.png" alt="Google+" title="Google+" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"></a></td>
                                                                                                                                        </tr>
                                                                                                                                </tbody>
                                                                                                                        </table>
                                                                                                                </td>
                                                                                                        </tr>
                                                                                                </tbody>
                                                                                        </table>
                                                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                                                                <tbody>
                                                                                                        <tr style="vertical-align: top;" valign="top">
                                                                                                                <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #BBBBBB; width: 100%;" align="center" role="presentation" valign="top">
                                                                                                                                <tbody>
                                                                                                                                        <tr style="vertical-align: top;" valign="top">
                                                                                                                                                <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
                                                                                                                                        </tr>
                                                                                                                                </tbody>
                                                                                                                        </table>
                                                                                                                </td>
                                                                                                        </tr>
                                                                                                </tbody>
                                                                                        </table>
                                                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                                                        <div style="color:#fcfcfc;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                                                                <div style="line-height: 1.2; font-size: 12px; color: #fcfcfc; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 14px;">
                                                                                                        <p style="text-align: center; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;">Copyright © 2020 IEEE Student Branch Manipal, All rights reserved.</p>
                                                                                                        <p style="text-align: center; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;">&nbsp;</p>
                                                                                                        <p style="text-align: center; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;">Where to find us:<br>contactus.ieeesbmanipal@gmail.com</p>
                                                                                                </div>
                                                                                        </div>
                                                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                                                                <tbody>
                                                                                                        <tr style="vertical-align: top;" valign="top">
                                                                                                                <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #BBBBBB; width: 100%;" align="center" role="presentation" valign="top">
                                                                                                                                <tbody>
                                                                                                                                        <tr style="vertical-align: top;" valign="top">
                                                                                                                                                <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
                                                                                                                                        </tr>
                                                                                                                                </tbody>
                                                                                                                        </table>
                                                                                                                </td>
                                                                                                        </tr>
                                                                                                </tbody>
                                                                                        </table>
                                                                                        <!--[if (!mso)&(!IE)]><!-->
                                                                                </div>
                                                                                <!--<![endif]-->
                                                                        </div>
                                                                </div>
                                                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                                        </div>
                                                </div>
                                        </div>
                                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                </td>
                        </tr>
                </tbody>
        </table>
        <!--[if (IE)]></div><![endif]-->
</body>

</html>'''


#The mail addresses and password
sender_address = 'contactus@ieeemanipal.com'
sender_pass = '********'


#Reading the csv for attachments and emails
col_list = ['Email', 'Attachment Name']
df = pd.read_csv('mailswithAttachments.csv', usecols=col_list)

# print(df['Attachment Name'])

receiver_address = pd.array(df['Email'])
attachment_names = pd.array(df['Attachment Name'])


if(len(receiver_address) != len(attachment_names)):
        print("Attachment Names are not equal to receiver emails.")
        exit

if len(receiver_address) == 0 :
    print('There are no receiver emails')
    exit



rootpath = os.path.abspath(os.path.dirname(__file__))
# print(os.path.join(rootpath, attachment_names[0]))


try:
    for i in range(len(receiver_address)):
        try:
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address[i]
            message['Subject'] = 'IEEE SBM | ManComm Certificate of Appreciation'
            #The subject line

        
            #The body and the attachments for the mail, Use 'plain' if only plain text, use 'html' if sending html page
            # message.attach(MIMEText(mail_content, 'plain'))
            message.attach(MIMEText(mail_content, 'html'))


            #Comment out next 11 lines if not to send an attachment
            attach_file_name = os.path.join(rootpath, attachment_names[i])
            attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload) #encode the attachment


            #add payload header with filename
            payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attach_file_name))
            message.attach(payload)
            print(os.path.basename(attach_file_name))

        
            #Create SMTP session for sending the mail
            temp = sender_address.split('@')
            if temp[1] == "ieeemanipal.com":
                session = smtplib.SMTP('smtp.zoho.eu', 587)
            elif temp[1] == "gmail.com":
            	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            elif temp[1] == "outlook.com" or temp[1] == "hotmail.com" :
                session = smtplib.SMTP('smtp-mail.outlook.com', 587)
            elif temp[1] == "yahoo.in" or temp[1] == "yahoo.com" :
                session = smtplib.SMTP('smtp.mail.yahoo.com', 587)
            else :
                print("This Application only supports gmail, yahoo mail, hotmail and outlook mailing")
                exit

            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address[i], text)
            session.quit()

            print('Mail Sent to ' + receiver_address[i])

        except SMTPRecipientsRefused:
            print('Invalid Receiver Email: ' + receiver_address[i])

except SMTPAuthenticationError:
    print('The Username and/or Password of sender mail you entered is incorrect')

# except Exception:
#     print("Something doesn't seem right, Try Again.")



