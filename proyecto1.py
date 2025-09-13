import pandas as pd
import matplotlib.pyplot as plt

# Cleaning data / Limpiando datos
# Setting max rows / Seteamos la maxima cantidad de filas

pd.options.display.max_rows = None
# Getting the file / Traigo el archivo
df = pd.read_csv('Python/archive/data.csv', encoding = 'latin1')
# Delete null entries / Eliminar entradas nulas
df.dropna(inplace= True)
# Format date / Formateo fechas
df['Order Date'] = pd.to_datetime(df['Order Date'], format = 'mixed')
df['Ship Date']  = pd.to_datetime(df['Ship Date'], format = 'mixed')

# Sales mean / Promedio de ventas
sales_mean = round(df['Sales'].mean(), 2)
print(f'Sales mean: $ {sales_mean}')

# Profit mean / Promedio de superavit

profit_mean = round(df['Profit'].mean(), 2)
print(f'Profit mean: $ {profit_mean}')

# Sales median / mediana de ventas
sales_median = round(df['Sales'].median() , 2)
print(f'Sales median: $ {sales_median}')

# Profit median / Mediana de superavit
profit_median = round(df['Profit'].median(), 2)
print(f'Profit median: $ {profit_median}')

# Total sales / Ventas totales
total_sales = round(df['Sales'].sum(), 2)
print(f'Total sales: $ {total_sales}')

# Total profit / superavit total
total_profit = round(df['Profit'].sum(), 2)
print(f'Total profit: $ {total_profit}')

# Region distribution / distribucion por region
region_stats = pd.DataFrame({
    'Count': df['Region'].value_counts(),
    'Percentage': df['Region'].value_counts(normalize=True) * 100
})

plt.bar(region_stats.index, region_stats['Percentage'])
plt.xlabel('Region')
plt.ylabel('Percentage (%)')
plt.title('Region Distribution (%)')
plt.show()

# Category distribution / distribucion por categoria

category_stats_percentage = pd.DataFrame({
    'Count': df['Category'].value_counts(),
    'Percentage': df['Category'].value_counts(normalize=True) * 100
})

category_stats = pd.DataFrame({
    'Count': df['Category'].value_counts(),
    'Quantity': df['Category'].value_counts()
})

plt.bar(category_stats_percentage.index, category_stats_percentage['Percentage'])
plt.xlabel('Category')
plt.ylabel('Percetage (%)')
plt.title('Category distribution (%)')
plt.show()

plt.bar(category_stats.index, category_stats['Quantity'])
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.title('Quantity per category')
plt.show()

# Sub-category distribution / distribucion por sub-categoria

sub_category_stats = pd.DataFrame({
    'Count': df['Sub-Category'].value_counts(),
    'Percentage': df['Sub-Category'].value_counts(normalize=True) * 100
})

plt.figure(figsize=(8,10))  # más alto
plt.barh(sub_category_stats.index, sub_category_stats['Percentage'])
plt.xlabel('Percentage (%)')
plt.ylabel('Sub-Categories')
plt.title('Sub-categories distribution (%)')
plt.show()

# Group sales by day / Agrupo ventas por dia

sales_over_time = df.groupby('Order Date')['Sales'].sum()

plt.plot(sales_over_time.index, sales_over_time.values)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales evolution through dates')
plt.show()

# Relation between discount and profit / Relacion entre descuentos y beneficio

correlation = df['Discount'].corr(df['Profit'])

plt.scatter(df['Discount'], df['Profit'], alpha=0.5)
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.title('Relation: Discount vs Profit')
plt.text( 0.05,                          
    df['Profit'].max() * 0.9,      
    f'Correlation: {correlation:.2f}',
    fontsize=12,
    bbox=dict(facecolor='white', alpha=0.7))
plt.show()

# Top sellers / Top vendedores

sales_by_customer = df.groupby('Customer Name')['Sales'].sum()
sales_by_customer = sales_by_customer.sort_values(ascending=False)
top10_customers = sales_by_customer.head(10)
top10_customers.plot(kind='bar', figsize=(10,6))
plt.xlabel('Customer')
plt.ylabel('Total Sales')
plt.title('Top 10 Sellers')
plt.xticks(rotation=45, ha='right')
plt.show()
