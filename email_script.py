import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from smtplib import SMTPAuthenticationError, SMTPRecipientsRefused
import csv


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
											<div style="color:#c60888;font-family:Georgia, Times, 'Times New Roman', serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:0px;padding-left:10px;">
												<div style="line-height: 1.2; font-size: 12px; font-family: Georgia, Times, 'Times New Roman', serif; color: #c60888; mso-line-height-alt: 14px;">
													<p style="font-size: 14px; line-height: 1.2; word-break: break-word; text-align: center; font-family: Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 17px; margin: 0;"><strong><span style="font-size: 26px;">EXODUS</span></strong></p>
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
								<!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
								<div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
									<div style="width:100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
											<!--<![endif]-->
											<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 0px; padding-bottom: 10px; font-family: Georgia, 'Times New Roman', serif"><![endif]-->
											<div style="color:#393d47;font-family:Georgia, Times, 'Times New Roman', serif;line-height:1.2;padding-top:0px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
												<div style="line-height: 1.2; font-size: 12px; font-family: Georgia, Times, 'Times New Roman', serif; color: #393d47; mso-line-height-alt: 14px;">
													<p style="font-size: 18px; line-height: 1.2; word-break: break-word; text-align: center; font-family: Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 22px; margin: 0;"><span style="font-size: 18px;"><strong>A Front-End Web Dev Challenge</strong></span></p>
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
											<div class="img-container center fixedwidth fullwidthOnMobile" align="center" style="padding-right: 0px;padding-left: 0px;">
												<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img class="center fixedwidth fullwidthOnMobile" align="center" border="0" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/583187_564778/WhatsApp%20Image%202020-09-25%20at%209.09.10%20PM.jpeg" alt="Alternate text" title="Alternate text" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 325px; display: block;" width="325">
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
													<p style="font-size: 17px; line-height: 1.2; word-break: break-word; text-align: justify; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; mso-line-height-alt: 20px; mso-ansi-font-size: 18px; margin: 0;"><span style="font-size: 17px; mso-ansi-font-size: 18px;">Thank you for registering for EXODUS. The competition is scheduled for 2nd to 4th October 2020. Rule Book for the event shall be released on 1st October post 2 PM on the WhatsApp group where all further communication will be taking place between organizers and the participants. Teams not present in this official group shall be considered out from the competition. </span><em><span style="font-size: 17px; mso-ansi-font-size: 18px;">Please join the WhatsApp group using the following link for more updates if you haven't already:</span></em></p>
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
											<div class="button-container" align="center" style="padding-top:0px;padding-right:10px;padding-bottom:0px;padding-left:10px;">
												<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 0px; padding-right: 10px; padding-bottom: 0px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://chat.whatsapp.com/FE9DywCw3IYCDEI7AWHTnC" style="height:34.5pt; width:157.5pt; v-text-anchor:middle;" arcsize="27%" strokeweight="0.75pt" strokecolor="#8a3b8f" fillcolor="#00e676"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Arial, sans-serif; font-size:16px"><![endif]--><a href="https://chat.whatsapp.com/FE9DywCw3IYCDEI7AWHTnC" target="_blank" style="-webkit-text-size-adjust: none; text-decoration: none; display: inline-block; color: #ffffff; background-color: #00e676; border-radius: 12px; -webkit-border-radius: 12px; -moz-border-radius: 12px; width: auto; width: auto; border-top: 1px solid #8a3b8f; border-right: 1px solid #8a3b8f; border-bottom: 1px solid #8a3b8f; border-left: 1px solid #8a3b8f; padding-top: 10px; padding-bottom: 10px; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; text-align: center; mso-border-alt: none; word-break: keep-all;"><span style="padding-left:10px;padding-right:10px;font-size:16px;display:inline-block;"><span style="font-size: 16px; line-height: 1.5; word-break: break-word; mso-line-height-alt: 24px;"><strong>Join WhatsApp Group</strong></span></span></a>
												<!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
											</div>
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
													<p style="text-align: center; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;">Copyright ?? 2020 IEEE Student Branch Manipal, All rights reserved.</p>
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
sender_address = 'ieeesbm.events@gmail.com'
sender_pass = '*******'


with open('mails.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

print(data[0])

receiver_address = data[0]

# receiver_address = ['kumaridk123@gmail.com']

if receiver_address == [] :
    print('There are no receiver emails')
    exit

try:
    for receiver in receiver_address:
        try:
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver
            message['Subject'] = 'EXODUS: WhatsApp Group Invite Link'
            #The subject line


            #The body and the attachments for the mail, Use 'plain' if only plain text, use 'html' if sending html page
            # message.attach(MIMEText(mail_content, 'plain'))
            message.attach(MIMEText(mail_content, 'html'))


            #Comment out next 11 lines if not to send an attachment
            # attach_file_name = '../DemoProjects/GitHub-Mark/PNG/GitHub-Mark-32px.png'
            # attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
            # payload = MIMEBase('application', 'octate-stream')
            # payload.set_payload((attach_file).read())
            # encoders.encode_base64(payload) #encode the attachment


            # #add payload header with filename
            # payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attach_file_name))
            # message.attach(payload)
            # print(os.path.basename(attach_file_name))


            #Create SMTP session for sending the mail
            temp = sender_address.split('@')
            if temp[1] == "gmail.com":
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
            session.sendmail(sender_address, receiver, text)
            session.quit()

            print('Mail Sent to ' + receiver)

        except SMTPRecipientsRefused:
            print('Invalid Receiver Email: ' + receiver)

except SMTPAuthenticationError:
    print('The Username and/or Password of sender mail you entered is incorrect')

# except Exception:
#     print("Something doesn't seem right, Try Again.")



