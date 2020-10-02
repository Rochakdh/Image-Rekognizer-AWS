from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView
from .forms import ImageForm
from .models import Image
from django.urls import reverse_lazy
from django.conf import settings
# Create your views here.


class GetImage(CreateView):
    # model = Image
    template_name = 'rekon/index.html'
    success_url = reverse_lazy('rekon:index')
    form_class = ImageForm

    def get_context_data(self, **kwargs):
        print("---------------->>>>>>>>>>")
        context = super(GetImage, self).get_context_data(**kwargs)
        context['pic'] = Image.objects.latest('id')
        get_url = "{}{}".format(settings.MEDIA_URL,Image.objects.latest('id').image)
        # print(Image.objects.latest('id').image)
        get_response = imgrekon(get_url)
        context['gender'] = get_response.get('gender')
        context['lowage'] =  get_response.get('lowage')
        context['highage'] =  get_response.get('highage')
        context['emotion'] =  get_response.get('emotion')
        context['smile'] =  get_response.get('smile')
        context['eyeglass'] = get_response.get('eyeglass')
        context['sunglasses'] = get_response.get('sunglasses')
        context['mustache'] = get_response.get('mustache')
        context['eye'] = get_response.get('eye')
        context['mouthopen'] = get_response.get('mouthopen')
        context['mouthclose'] = get_response.get('mouthclose')
        return context



def imgrekon(img_url):
    import boto3

    import json

    # Change photo to the path and filename of your image.
    parse_url = str(img_url)[1:]
    photo = parse_url
    parsed_data = {}
    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:

        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])

    # print(response)

    print('Detected faces for ' + photo)
    for faces in response['FaceDetails']:
        parsed_data['gender'] = faces['Gender'].get('Value')
        parsed_data['lowage'] = faces['AgeRange'].get('Low')
        parsed_data['highage'] = faces['AgeRange'].get('High')
        parsed_data['emotion'] = faces['Emotions'][0].get('Type')

        # print(faces['AgeRange'].get('Low'))
        # print(faces['AgeRange'].get('High'))

        print(faces['Emotions'][0].get('Type'))
        if faces['Smile'].get('Value'):
            parsed_data['smile'] = "smile"
        if faces['Eyeglasses'].get('Value'):
            parsed_data['eyeglass'] = "eyeglasses"
        if faces['Sunglasses'].get('Value'):
            parsed_data['sunglasses'] = "sunglasses"
        if faces['Mustache'].get('Value'):
            parsed_data['mustache'] = "mustache"
        if faces['EyesOpen'].get('Value'):
            parsed_data['eye'] = "eyes open"
        if faces['MouthOpen'].get('Value'):
            parsed_data['mouthopen'] = "Mouth open"
        if faces['MouthOpen'].get('Value') is False:
            parsed_data['mouthclose'] = "Mouth close"
        return (parsed_data)




