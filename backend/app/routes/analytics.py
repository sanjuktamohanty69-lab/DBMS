from flask import Blueprint, jsonify

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics/low-stock', methods=['GET'])
def low_stock_products():
    # Logic to fetch and return low stock products
    return jsonify({'message': 'Low stock products data'}), 200

@analytics_bp.route('/analytics/top-products', methods=['GET'])
def top_products_by_sales():
    # Logic to fetch and return top products by sales
    return jsonify({'message': 'Top products by sales data'}), 200

@analytics_bp.route('/analytics/customer-sales', methods=['GET'])
def customer_sales_analysis():
    # Logic to fetch and return customer sales analysis
    return jsonify({'message': 'Customer sales analysis data'}), 200

@analytics_bp.route('/analytics/restock-history', methods=['GET'])
def restock_history_by_supplier():
    # Logic to fetch and return restock history by supplier
    return jsonify({'message': 'Restock history by supplier data'}), 200
