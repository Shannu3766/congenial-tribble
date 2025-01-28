from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (nested JSON)
data = {
    "deals": {
        0:{"deal_title": "Wireless Bluetooth Earbuds Pro", "deal_photo": "https://imgs.search.brave.com/2HBlXLMLal__X5Be9lmi8hnJFb5SopCOyDk8M3KFAH4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NDFXR3B3aE5kMUwu/anBn", "deal_starts_at": "12-02-2025"},
        1:{"deal_title": "Smart LED Desk Lamp with Touch Control", "deal_photo": "https://imgs.search.brave.com/QynJBwcKHGF3kavGqx9DOMrbHxwyl6tI2vinc-Leu-E/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/dGhld2lyZWN1dHRl/ci5jb20vd3AtY29u/dGVudC9tZWRpYS8y/MDI0LzAxL2xlZGRl/c2tsYW1wcy0yMDQ4/cHgtemJhcm1pbmku/anBnP2F1dG89d2Vi/cCZxdWFsaXR5PTc1/JndpZHRoPTEwMjQ", "deal_starts_at": "15-01-2025"},
        2:{"deal_title": "4K Ultra HD Smart TV 65 inch", "deal_photo": "https://imgs.search.brave.com/39CHYktXVzPIjeUlMebyuI6b34xIR8CGHf9tSEoBAMI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZS11cy5zYW1zdW5n/LmNvbS9TYW1zdW5n/VVMvaG9tZS90ZWxl/dmlzaW9uLWhvbWUt/dGhlYXRlci90dnMv/Y3J5c3RhbC11aGQt/dHZzLzExMDExMjAy/NC9EVTcyMDBfQ3J5/c3RhbF9VSERfTEVG/VF8xNjAweDEyMDAu/anBnPyRwcm9kdWN0/LWRldGFpbHMtanBn/JA", "deal_starts_at": "20-03-2025"},
        3:{"deal_title": "Noise Cancelling Over-Ear Headphones", "deal_photo": "https://imgs.search.brave.com/lvVsyf1f6QeT0ap6hvBrZxFVImXIuVe2Egu-3T-UkJE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/c2hvcGlmeS5jb20v/cy9maWxlcy8xLzA1/MTYvMzc2MS82ODMw/L3Byb2R1Y3RzLzNf/ZmNkNjY5MTYtM2Y3/Ny00NGZiLWJkZmEt/YjM2MzgzMDVkMzMx/LmpwZz92PTE2NTAw/MTYwMDY", "deal_starts_at": "22-01-2025"},
        4:{"deal_title": "Portable Bluetooth Speaker 360° Sound", "deal_photo": "https://imgs.search.brave.com/h5j2rpc1hSH461PhP9xVexkC0GnpZhA8AzjviKu-FMk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5jbm4uY29tL2Fw/aS92MS9pbWFnZXMv/c3RlbGxhci9wcm9k/L3NvbnktdWx0LWZp/ZWxkLTEtcHJvZHVj/dC1jYXJkLWNubnUu/anBnP2M9MTZ4OSZx/PWhfNzIwLHdfMTI4/MCxjX2ZpbGw", "deal_starts_at": "01-02-2025"},
        5:{"deal_title": "Smart Fitness Tracker with Heart Rate Monitor", "deal_photo": "https://imgs.search.brave.com/F7a1v_E65_Cyr3_40owWsy9YWOA_RveUZwU-hVbrGwM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5jbm4uY29tL2Fw/aS92MS9pbWFnZXMv/c3RlbGxhci9wcm9k/L2ZpdGJpdC1pbnNw/aXJlLTMtcGMtY25u/dS5qcGc_Yz0xNng5/JnE9aF83MjAsd18x/MjgwLGNfZmlsbA", "deal_starts_at": "05-01-2025"},
        6:{"deal_title": "Smart Thermostat with Voice Control", "deal_photo": "https://imgs.search.brave.com/vdrbeWqN9KSX-I6j-3e8YR_yl3_hjhZ317THLRT8crA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9leHBl/cmNvbS5jb20vY2Ru/L3Nob3AvcHJvZHVj/dHMvMTA2MjcxMTEw/NC5qcGc_dj0xNjE5/NzI2Mjk0JndpZHRo/PTE0NDU", "deal_starts_at": "10-03-2025"},
        7:{"deal_title": "Electric Coffee Grinder with Adjustable Settings", "deal_photo": "https://imgs.search.brave.com/0u6Rzqircp1Jjigc6s-pyuNJsYjThHjqLt9h5dKef_0/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NjFDcTRsOXRMMEwu/anBn", "deal_starts_at": "30-01-2025"},
        8:{"deal_title": "High Performance Gaming Laptop 16GB RAM", "deal_photo": "https://imgs.search.brave.com/BSwQJXDWRKNkxcWuG1hWw5ewERSbLSS_7kMIlWT8t5s/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/dGhld2lyZWN1dHRl/ci5jb20vd3AtY29u/dGVudC9tZWRpYS8y/MDI0LzExL2NoZWFw/Z2FtaW5nbGFwdG9w/cy0yMDQ4cHgtNzk4/MS0xLmpwZz9hdXRv/PXdlYnAmcXVhbGl0/eT03NSZ3aWR0aD0x/MDI0", "deal_starts_at": "23-02-2025"},
        9:{"deal_title": "2-in-1 Smartwatch with Fitness Tracker", "deal_photo": "https://imgs.search.brave.com/Eu_w1WNLlBurjGfEHtuElYpq4xtcfs_0M19vVLwXm-s/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMtbmEuc3NsLWlt/YWdlcy1hbWF6b24u/Y29tL2ltYWdlcy9J/LzYxUTRwNElVeGxM/LmpwZw", "deal_starts_at": "17-03-2025"},
        10:{"deal_title": "Wireless Charging Pad for Smartphones", "deal_photo": "https://imgs.search.brave.com/ZNDpClQDkJfnBilVoUj59u4haMFG14-HYJi4ctkY5tY/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NjFSK3cyNGZHZEwu/anBn", "deal_starts_at": "09-01-2025"},
        11:{"deal_title": "Portable Power Bank 20000mAh", "deal_photo": "https://imgs.search.brave.com/pB96n_7hEU8CxWTir1z2d_n7oo3-0dWK72VHsHnxj_o/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jMS5u/ZXdlZ2dpbWFnZXMu/Y29tL3Byb2R1Y3Rp/bWFnZS9uYjMwMC9B/TTVXUzIzMDcwMzBZ/RkxXWDYxLmpwZw", "deal_starts_at": "19-02-2025"},
        12:{"deal_title": "Waterproof Bluetooth Earphones", "deal_photo": "https://imgs.search.brave.com/eXiyyw8bBgbC1GipXwXnl9e6UDTOVK-LOrL1qWNacvE/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NzFoQ2JjZUg5LUwu/anBn", "deal_starts_at": "25-01-2025"},
        13:{"deal_title": "Smart LED Strip Lights with Remote", "deal_photo": "https://imgs.search.brave.com/TXbqZXLzpbxmlEMD6ikCK6WwXO1L_5N5zyNauafPT0M/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMucHJpc21pYy5p/by9rYXNhc21hcnQv/YjhmMDY4NzItZDJk/NS00NjI0LTk4NTkt/ZDNmNjMxMTMyOGI4/X0tMNDMwX0NvbG9y/cytab25lc19LYXNh/c21hcnRfRG90X0Nv/bS5wbmc_YXV0bz1j/b21wcmVzcyxmb3Jt/YXQmcmVjdD0wLDAs/MjAwMCwyMDAwJnc9/MTAwMCZoPTEwMDA", "deal_starts_at": "07-03-2025"},
        14:{"deal_title": "Electric Toothbrush with Smart Timer", "deal_photo": "https://imgs.search.brave.com/s8fYp_H_upaRVSlZcnTHjxI9S4TXMzXZ1r17gKI4WiY/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5jbm4uY29tL2Fw/aS92MS9pbWFnZXMv/c3RlbGxhci9wcm9k/L29yYWwtYi1nZW5p/dXMuanBnP2M9MTZ4/OSZxPWhfNzIwLHdf/MTI4MCxjX2ZpbGw", "deal_starts_at": "11-02-2025"}
    }
}

@app.route('/fetch_details', methods=['GET'])
def fetch_details():
    try:
        # Get the 'page' parameter from the query string (defaults to 1 if not provided)
        page = int(request.args.get('page', 1))
        
        # Set the number of records per page
        records_per_page = 10
        
        # Convert the 'deals' dictionary to a list and calculate the start and end index based on the page
        deals_list = list(data['deals'].values())
        start_idx = (page - 1) * records_per_page
        end_idx = start_idx + records_per_page
        
        # Extract the deals for the current page
        deals = deals_list[start_idx:end_idx]
        
        # If no records are found for the page, return an empty list
        if not deals:
            return jsonify({"message": "No records found"}), 404
        
        # Return the fetched records as a JSON response
        return jsonify(deals)
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # app.run(debug=True)
     app.run(host='0.0.0.0', port=5000, debug=True)
