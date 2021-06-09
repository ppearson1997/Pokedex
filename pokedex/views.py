from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from django.shortcuts import render,redirect, get_object_or_404
from . import models, forms
from django.contrib import messages 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,   UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Custom_Pagination(object):

    def __init__(self, queryset, numb_pages, request_page):
        self.queryset = queryset           
        self.numb_pages = numb_pages
        self.request_page = request_page        

    def pagination(self):
        paginator = Paginator(self.queryset, self.numb_pages)
        page = self.request_page
        try:
            list_items = paginator.page(page)
        except PageNotAnInteger:
            list_items = paginator.page(1)
        except EmptyPage:
            list_items = paginator.page(paginator.numb_pages)

        index = list_items.number - 1
        limit = 5 
        max_index = len(paginator.page_range)
        start_index = index - limit if index >= limit else 0
        end_index = index + limit if index <= max_index - limit else max_index
        page_range = paginator.page_range[start_index:end_index]
        return page_range


class PokedexListView(ListView):
    model = models.Pokemon
    template_name = 'pages/pokemon_list.html'
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context_data = super(PokedexListView, self).get_context_data(**kwargs)
        context_data['page_range'] = Custom_Pagination(self.get_queryset(), self.paginate_by, self.request.GET.get('page',1)).pagination()
        return context_data


class PokedexDetailView(DetailView):
    model = models.Pokemon
    template_name = 'pages/pokemon_detail.html'
    
    def get(self, request, *args, **kwargs):
        data = get_object_or_404(models.Pokemon, pk=kwargs['pk'])
        if data:
            type = models.PokemonTypeSlot.objects.filter(pokemon=data.id)
            ability = models.PokemonAbilitySlot.objects.filter(pokemon=data.id)
            context = { 
                    'data': data,
                    'type': type,
                    'ability': ability
                }
        print(context, data.id)
        return render(request, self.template_name, context)


class PokedexCreateView(CreateView):
    form_class= forms.PokedexForm
    template_name = 'pages/pokemon_create.html'
    success_url = '/'
    
    def post(self, request, form):
        super(PokedexCreateView, self).post(request)
        try:
            if form.is_valid:
                pokemon = models.Pokemon.objects.get(id=self.object.id)
                type_slot = request.POST['type_slot'].split(",")
                ability_slot = request.POST['ability_slot'].split(",")
                for type in request.POST.getlist('type'):
                    pokemontype = models.PokemonType.objects.get(id=type)
                    pokemontypeslot, created = models.PokemonTypeSlot.objects.get_or_create(type = pokemontype, pokemon=pokemon,
                                                                                    slot = type_slot[request.POST.getlist('type').index(type)])

                for ability in request.POST.getlist('ability'):
                    pokemonability = models.PokemonAbility.objects.get(id=ability)
                    pokemonabilityslot, created = models.PokemonAbilitySlot.objects.get_or_create(ability = pokemonability, pokemon=pokemon,
                                                                                        slot = ability_slot[request.POST.getlist('ability').index(ability)])
            else:
                messages.error(request, "Error")
        except Exception as e: 
            print(e)
        
        return redirect(self.success_url)