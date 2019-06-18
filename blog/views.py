from django.shortcuts import render

assignments = [
    {
        'title': 'calculus-7cdb',
        'content': ['crowdmark-exam-fd969', 'test-2-crowdmark-5e727', 'tutorial-7-fiscal'],
        'num_content': 3
    },
    {
        'title': 'linear-algebra-fall-2017',
        'content': ['tutorial-8-money-and-banking', 'tutorial-6-as-ad'],
        'num_content': 2
    }
]

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]

def home(request):
    context = {
        'assignments': assignments
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
