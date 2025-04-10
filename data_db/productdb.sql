USE productdb;
SELECT * FROM brands, products, categories
WHERE brands.brand_id = products.brand_id
OR categories.category_id = products.category_id;

SELECT * FROM staffs, stocks, stores
WHERE staffs.store_name = stocks.store_name
OR stores.email = staffs.email;
