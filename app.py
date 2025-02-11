from flask import Flask, jsonify, request
import json
app = Flask(__name__)

data = {
    "deals": {
        0: {"id":"01","deal_title": "House warming cermony", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj0qYJO3lkf7cdnjGkNtBLPz9UA-u65XvFn4mZxSaE2ajWxeyMPidNzD7PaSX6F1Afd0o", "deal_starts_at": "2025-02-02", "time": "09:00:00"},
        1: {"id":"02","deal_title": "Birthday Clelebrations", "deal_photo": "https://imgs.search.brave.com/QynJBwcKHGF3kavGqx9DOMrbHxwyl6tI2vinc-Leu-E/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/dGhld2lyZWN1dHRl/ci5jb20vd3AtY29u/dGVudC9tZWRpYS8y/MDI0LzAxL2xlZGRl/c2tsYW1wcy0yMDQ4/cHgtemJhcm1pbmku/anBnP2F1dG89d2Vi/cCZxdWFsaXR5PTc1/JndpZHRoPTEwMjQ", "deal_starts_at": "2025-02-20", "time": "10:00:00"},
        2: {"id":"03","deal_title": "Wedding aniversary", "deal_photo": "https://imgs.search.brave.com/39CHYktXVzPIjeUlMebyuI6b34xIR8CGHf9tSEoBAMI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZS11cy5zYW1zdW5n/LmNvbS9TYW1zdW5n/VVMvaG9tZS90ZWxl/dmlzaW9uLWhvbWUt/dGhlYXRlci90dnMv/Y3J5c3RhbC11aGQt/dHZzLzExMDExMjAy/NC9EVTcyMDBfQ3J5/c3RhbF9VSERfTEVG/VF8xNjAweDEyMDAu/anBnPyRwcm9kdWN0/LWRldGFpbHMtanBn/JA", "deal_starts_at": "2025-02-02", "time": "11:00:00"},
        3: {"id":"04","deal_title": "Job Interview ", "deal_photo": "https://stylegirlfriend.com/wp-content/uploads/2019/03/corporate-job-interview-outfits.png", "deal_starts_at": "2025-02-20", "time": "11:00:00"},
        4: {"id":"05","deal_title": "Engagement Party", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU5n3lp73hD5qVvHAGWejOECfsaMH7v5CnmSTe7ZTwkIeev4TlpD78b9WQZtDEhd0VHxI", "deal_starts_at": "2025-03-20", "time": "13:00:00"},
        5: {"id":"06","deal_title": "Corporate Meetings & Conferences", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsp_q54aXCQBQ5z19j3UGd_n0UA-9EFR1Ovg&s", "deal_starts_at": "2025-02-05", "time": "14:00:00"},
        6: {"id":"07","deal_title": "Enagagement Parties", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU5n3lp73hD5qVvHAGWejOECfsaMH7v5CnmSTe7ZTwkIeev4TlpD78b9WQZtDEhd0VHxI", "deal_starts_at": "2025-02-15", "time": "15:00:00"},
        7: {"id":"08","deal_title": "Public Speaking Events", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIkBho-CM_to24BfAX583jTmNr4kb5jv3UnqirPqPejJtYglOj2tbwgNrmP-pkknNdAgw", "deal_starts_at": "2025-02-12", "time": "16:00:00"},
        8: {"id":"09","deal_title": "Diwali Celebrations", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpFvNz2Tv3d7ET0o_ONKlXKJnkpPQxGd_QrVt69UkIx3m6V1Q8vZZhZHMqH-dTDwvtUNs", "deal_starts_at": "2025-03-05", "time": "17:00:00"},
        9: {"id":"10","deal_title": "Graduation Ceremonies", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREk_tagol9D7Z1oUXIb_Uq1z40pAzbu1pvMXpfxHPY8jXr8XyZfpWf652NCsUUQJd_WBI", "deal_starts_at": "2025-03-02", "time": "18:00:00"},
        10: {"id":"11","deal_title": "Eid Celebrations", "deal_photo": "https://imgs.search.brave.com/iEsO2uj4sfeTHN0niLdV1UT2zyYpDQJkv1P2da8t-L4/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YXMudXRzYXZmYXNo/aW9uLmNvbS9tZWRp/YS93eXNpd3lnL3By/b21vdGlvbnMvMjAy/NC8xNjA1L2VpZC1w/YWdlc18xNC5qcGc", "deal_starts_at": "2025-03-03", "time": "19:00:00"},
        11: {"id":"12","deal_title": "Gurdwara Service & Amrit Ceremony", "deal_photo": "https://imgs.search.brave.com/ptw3tdkuHxB6UBpfXy0FFIesljMbC36P_dbTrGSN-aU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/c2hvcGlmeS5jb20v/cy9maWxlcy8xLzA5/ODEvODE3OC9maWxl/cy9uZXV0cmFscy1v/dXRmaXQtbGlnaHQt/Z3JleS11dGlsaXR5/LXNoaXJ0LmpwZz84/MTM3NDkzOTUxNjYw/MjI2NDg4","deal_starts_at": "2025-03-11", "time": "20:00:00"},
        12: {"id":"13","deal_title": "First Dates", "deal_photo": "https://www.stylebysavina.com/wp-content/uploads/2023/06/what-to-wear-on-a-casual-first-date-female.jpg", "deal_starts_at": "2025-03-12", "time": "21:00:00"},
        13: {"id":"14","deal_title": "Funerals", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRupLtoNg4bf1PKltjzUrm71stNG7z5IElm1A&s", "deal_starts_at": "2025-03-20", "time": "22:00:00"},
        14: {"id":"15","deal_title": "Business Meetings", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsp_q54aXCQBQ5z19j3UGd_n0UA-9EFR1Ovg&s", "deal_starts_at": "2025-03-25", "time": "11:00:00"},
        15: {"id":"16","deal_title": "Diwali Celebrations", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpFvNz2Tv3d7ET0o_ONKlXKJnkpPQxGd_QrVt69UkIx3m6V1Q8vZZhZHMqH-dTDwvtUNs", "deal_starts_at": "2025-04-14", "time": "11:00:00"},
        16: {"id":"17","deal_title": "Job Interview ", "deal_photo": "https://stylegirlfriend.com/wp-content/uploads/2019/03/corporate-job-interview-outfits.png", "deal_starts_at": "2025-04-15", "time": "11:00:00"},
        17: {"id":"18","deal_title": "Engagement Parties", "deal_photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU5n3lp73hD5qVvHAGWejOECfsaMH7v5CnmSTe7ZTwkIeev4TlpD78b9WQZtDEhd0VHxI", "deal_starts_at": "2025-04-21", "time": "11:00:00"},
        18: {"id":"19","deal_title": "Gurdwara Service & Amrit Ceremony", "deal_photo": "https://imgs.search.brave.com/9fF6LKspU6fmYNoCA1UADkbv-tfChAW6VVrwZxmWBTU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/bW90dGFuZGJvdy5j/b20vY2RuL3Nob3Av/ZmlsZXMvT3V0Zml0/XzFfX0xpZ2h0LUto/YWtpLU1lcmNlci1K/ZWFuLUxpZ2h0LUdy/YXktU3RvbmUtSmVh/bi1DbGFzc2ljLUNy/ZXctRHJpZ2dzLVRl/ZS1XaGl0ZS1fNzUw/eDEwMDBfYTNlZDQx/ZGItNDM1Yi00MWU4/LWExMDAtYjZlN2My/YzJlYmE2LmpwZz92/PTE2OTQ0NTA5NTIm/d2lkdGg9NTMz", "deal_starts_at": "2025-04-22", "time": "11:00:00"},
        19: {"id":"20","deal_title": "Eid Celebrations", "deal_photo": "https://imgs.search.brave.com/KyCcmdBspTm02kE4-Cz3ab2JCZHfoqEIOyXUFGzL59Y/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/c2hvcGlmeS5jb20v/cy9maWxlcy8xLzA5/ODEvODE3OC9maWxl/cy9ibGFjay11dGls/aXR5LXNoaXJ0LW91/dGZpdDEuanBnPzEw/MzcxNDM2MzQ2NTcy/ODY4NDc", "deal_starts_at": "2025-04-20", "time": "11:00:00"},

    }
}


@app.route('/fetch_details', methods=['GET'])
def fetch_details():
    try:
        deals = list(data['deals'].values())
        if not deals:
            return jsonify({"message": "No records found"}), 404
        
        # Use json.dumps to return the full JSON
        response = app.response_class(
            response=json.dumps(deals, ensure_ascii=False, indent=4),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))  # Get the PORT from environment variable
    app.run(host="0.0.0.0", port= 5000, debug=True)