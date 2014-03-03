from bottle import route, run, template, get, post, request,delete,put
patient_record={}


  
@post('/patient/add')
def add_patient():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    store_info={}
    store_info["Name"] = p_name
    store_info["Gender"] = p_gender
    store_info["Age"] = p_age
    store_info["Address"] = p_address
    store_info["Phone"] = p_phone
    #store_info = ' '.join([p_name,p_gender,p_age,p_address,p_phone])
    patient_record.update({p_id:store_info})
    return patient_record

@get('/patient/show/<p_id>')
def show_patient(p_id):
    if p_id not in patient_record.keys():
        return 'This is not a correct patient id'
    else:
        return patient_record[p_id]

@put('/patient/update/<p_id>')
def patient_update(p_id):
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    store_info={}
    store_info["Name"] = p_name
    store_info["Gender"] = p_gender
    store_info["Age"] = p_age
    store_info["Address"] = p_address
    store_info["Phone"] = p_phone
    patient_record.update({p_id:store_info})
    return patient_record
   


@delete('/patient/delete/<p_id>')
def delete_patient(p_id):
    patient_record.pop(p_id)
    return patient_record


run(host='localhost',port=8080)
