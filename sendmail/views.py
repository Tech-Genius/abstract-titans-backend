from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from backend_api import settings

@csrf_exempt
def wlmail(request):
    if request.method == 'POST':
        x_username = request.POST['x_username'] or '--*--'
        comment_link = request.POST['comment_link'] or '--*--'
        discord_username = request.POST['discord_username'] or '--*--'
        evm = request.POST['evm'] or '--*--'
        why_titan = request.POST['why_titan'] or '--*--'
        # recipient_list = [request.POST.get('to_email')]
        if x_username and comment_link and discord_username and evm and why_titan:
          admin_deliver = 'X Username: \n' + x_username + '\n' + ' ' + '\n' + 'Comment Link: \n' + comment_link + '\n' + ' ' + '\n' + 'Discord Username: \n' + discord_username +  '\n' + ' ' + '\n' + 'EVM Wallet: \n' + evm + '\n' + ' ' + '\n' + 'Why Titan WL: \n' + why_titan 
          admin_subject = "New Abstract Titans WL Form Entry From " + x_username
          site_title = "Abstract Titans"
          send_mail(
            admin_subject,
            admin_deliver,
            settings.DEFAULT_FROM_EMAIL,
            ['wl-request@abstracttitans.xyz'],
            fail_silently= False
        )

        return JsonResponse({'message': 'Email sent successfully'})
    else:
      return JsonResponse({'Message': 'You need to make a post request'})    







