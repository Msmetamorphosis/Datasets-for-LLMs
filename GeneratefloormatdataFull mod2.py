import pandas as pd
import numpy as np
from datetime import timedelta, date


def random_dates(start, num_days, num_dates):
    return [start + timedelta(days=np.random.randint(num_days)) for _ in range(num_dates)]
def random_names(num_names):
    first_names = ['Jeff', 'Justin', 'Michael', 'Cindy', 'Tom', 'Laura', 'Chris', 'Sara', 'James', 'Wendy', 'Carla', 'Jessica', 'Jamie', 'Becky', 'Kevin']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Wilson', 'Martinez', 'Thompson', 'Matthews', 'Adkins', 'Scheck', 'Ferrer', 'Rivers', 'Gore', 'Evans']
    first_names.extend(['Mark', 'Sarah', 'Daniel', 'Rebecca', 'Paul', 'Mary', 'Thomas', 'Elizabeth', 'Charles', 'Jennifer', 'Matthew', 'Patricia', 'Donald', 'Linda']) 
    last_names.extend(['Anderson', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Campbell', 'Carter', 'Phillips'])
    return ["{} {}".format(np.random.choice(first_names), np.random.choice(last_names)) for _ in range(num_names)]
    return ["{} {}".format(np.random.choice(first_names), np.random.choice(last_names)) for _ in range(num_names)]

def random_addresses(num_addresses):
    streets = ['Oak', 'Maple', 'Pine', 'Cedar', 'Elm', 'Birch', 'Willow', 'Park', 'Forest', 'River', 'Hall', 'Cherry', 'Fir', 'Sequoia', 'Juniper', 'Holly', 'Aspen', 'Alder', 'Dogwood' ]
    streets.extend(['Amazon', 'Amber', 'Ambrose','Bierce','Ames','Amethyst','Amherst','Amity','Anderson','Andover','Andrew','Circular','Cityview','Clairview','Clara','Claremont','Clarence','Clarendon','Clarion','Clarke','Clarkson'])
    cities = ['Springfield', 'Rivertown', 'Eagleton', 'Maplewood', 'Brookside', 'Lakeside', 'Fairview', 'Crestview', 'Pleasanton', 'Hilltop', 'Clarksville', 'Nashville', 'Dade City', 'Bushnell', 'Ocala', 'Tampa', 'Silver Springs', 'Hopkinsville', 'Columbus']
    states = ['CA', 'TX', 'FL', 'NY', 'PA', 'IL', 'OH', 'GA', 'NC', 'MI', 'AZ', 'MS', 'WY', 'SD', 'NJ', 'AK', 'WV']
    zip_codes = [str(np.random.randint(10000, 99999)) for _ in range(num_addresses)]
    return ["{} {} St, {} {}, {}".format(np.random.randint(100, 999), np.random.choice(streets), np.random.choice(cities), np.random.choice(states), zip_code) for zip_code in zip_codes]



def random_items(num_items):
    items = ['Toyota Corolla 2015-2023', 'Toyota Camry 2017-2022', 'Volkwagen Passat 2018-2023', 'Toyota Highlander 2019-2024', 'Toyota Sienna 2015-2019', 'Toyota Sienna 2019-2023', 'Chevy Silverado 2019-2023']
    new_items = ['Toyota Highlander 2010-2015','Ford Expedition 2010-2017','Ford Expedition 2018-2023','Toyota Prius 2016-2023','Toyota Tundra 2015-2022'] 
    return [np.random.choice(items) for _ in range(num_items)]

def random_prices(num_prices, item_list):
    prices = {
        'Toyota Corolla 2015-2023': 33.96,
        'Toyota Camry 2017-2022': 33.96,
        'Volkwagen Passat 2018-2023': 33.96,        
        'Toyota Highlander 2019-2024': 49.95,
        'Toyota Sienna 2015-2019': 49.95,
        'Toyota Sienna 2019-2023': 49.95,
        'Chevy Silverado 2019-2023': 49.95,
        'Toyota Highlander 2010-2015': 49.95,
        'Ford Expedition 2010-2017': 49.95,
        'Ford Expedition 2018-2023': 49.95,
        'Toyota Prius 2016-2023': 33.96,
        'Toyota Tundra 2015-2022': 49.95
    }
    return [prices[item] for item in item_list]
   

def random_listing_numbers(num_listings):
    return [f"1000{np.random.randint(1000, 9999)}" for _ in range(num_listings)]

# Function to create a fake eBay dataset
def create_fake_ebay_dataset(num_rows=25):
    start_date = date.today()
    dates = sorted(random_dates(start_date, 30, num_rows))
    names = random_names(num_rows)
    addresses = random_addresses(num_rows)
    items = random_items(num_rows)
    unit_prices = random_prices(num_rows, items)
    quantities = np.random.randint(1, 5, size=num_rows)
    total_prices = [unit_prices[i] * quantities[i] for i in range(num_rows)]
    free_ship = np.random.choice(['Y', 'N'], num_rows)
    actual_shipping_costs = np.where(free_ship == 'Y', 0, np.random.uniform(7.75, 12.45, num_rows))
    listing_fees = np.random.uniform(0.25, 2.00, num_rows)
    paypal_fees = [0.30 + 0.029 * total for total in total_prices]
    item_costs = [unit_prices[i] * 0.4 * quantities[i] for i in range(num_rows)]  # Assuming cost is 40% of selling price
    listing_numbers = random_listing_numbers(num_rows)

    returns = np.random.choice(['Y','N'], size=num_rows, p=[0.2, 0.8]) 
    refunds = np.where(returns=='Y', np.random.uniform(0, total_prices), 0)
    df = pd.DataFrame({
        'Date': dates,
        'Customer Name': names,
        'Shipping Address': addresses,
        'Listing Number': listing_numbers,
        'Item/s Purchased': items,
        'Quantity': quantities,
        'Unit Price': unit_prices,
        'Total Purchase Price': total_prices,
        'Free Ship?': free_ship,
        'Actual Shipping Cost': actual_shipping_costs,
        'Listing Fee': listing_fees,
        'Paypal Fee': paypal_fees,
        'Item Cost': item_costs,
        'Returns': returns,
        'Refunds': refunds
    })
    
    return df


dataset = create_fake_ebay_dataset(125)

print(dataset.to_csv(sep='\t', index=False))
