from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Product

def product_review(request, product_id):
    # Retrieve product details from the database
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        # Process the submitted review form
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the review to the database
            review = form.save(commit=False)
            review.product = product
            review.save()
            # Redirect to the product detail page
            return redirect('product_detail', product_id=product_id)
    else:
        # Render the review form
        form = ReviewForm()
    
    # Get existing reviews for the product
    reviews = product.reviews.all()
    
    return render(request, 'product_review.html', {'product': product, 'form': form, 'reviews': reviews})
