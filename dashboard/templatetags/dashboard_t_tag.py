from django import template

register = template.Library() 


# This checkes if user is in a certain group
@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 



# Use this code in every template you want
# {% if request.user|has_group:"admin" %} 
#     <p>User belongs to admin
# {% else %}
#     <p>User doesn't belong to admin</p>
# {% endif %}