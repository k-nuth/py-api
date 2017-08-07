#import "transaction.h"

//uint32_t chain_transaction_version(transaction_t transaction);



PyObject* bitprim_native_chain_transaction_version(PyObject* self, PyObject* args){
    PyObject* py_transaction;  
    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }
    transaction_t transaction = (transaction_t)get_ptr(py_transaction);

    uint32_t res = chain_transaction_version(transaction);
    return Py_BuildValue("I", res);   


}


PyObject* bitprim_native_chain_transaction_set_version(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_transaction, &py_version)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    chain_transaction_set_version(transaction, py_version);

    Py_RETURN_NONE;   
}



PyObject* bitprim_native_chain_transaction_hash(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    hash_t res = chain_transaction_hash(transaction);
    return PyByteArray_FromStringAndSize(res.hash, 32);
}


PyObject* bitprim_native_chain_transaction_hash_sighash_type(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    uint32_t py_sighash_type;
    if ( ! PyArg_ParseTuple(args, "OI", &py_transaction, &py_sighash_type)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    hash_t res = chain_transaction_hash_sighash_type(transaction, py_sighash_type);
    return PyByteArray_FromStringAndSize(res.hash, 32);

}


PyObject* bitprim_native_chain_transaction_locktime(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    uint32_t res = chain_transaction_locktime(transaction);
    return Py_BuildValue("I", res);  
}

PyObject* bitprim_native_chain_transaction_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    int py_wire;
    if ( ! PyArg_ParseTuple(args, "Oi", &py_transaction, &py_wire)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    uint64_t res = chain_transaction_serialized_size(transaction, py_wire);
    return Py_BuildValue("K", res);
}


PyObject* bitprim_native_chain_transaction_fees(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    uint64_t res = chain_transaction_fees(transaction);
    return Py_BuildValue("K", res);  
}


PyObject* bitprim_native_chain_transaction_signature_operations(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    uint64_t res = chain_transaction_signature_operations(transaction);
    return Py_BuildValue("K", res);  
}

PyObject* bitprim_native_chain_transaction_signature_operations_bip16_active(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    int py_bip16_active;

    if ( ! PyArg_ParseTuple(args, "Oi", &py_transaction, &py_bip16_active)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    uint64_t res = chain_transaction_signature_operations_bip16_active(transaction, py_bip16_active);
    return Py_BuildValue("K", res);

}


PyObject* bitprim_native_chain_transaction_total_input_value(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    uint64_t res = chain_transaction_total_input_value(transaction);
    return Py_BuildValue("K", res);   
}

PyObject* bitprim_native_chain_transaction_total_output_value(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    uint64_t res = chain_transaction_total_output_value(transaction);
    return Py_BuildValue("K", res);   

}

PyObject* bitprim_native_chain_transaction_is_coinbase(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_coinbase(transaction);
    return Py_BuildValue("i", res);  
}

PyObject* bitprim_native_chain_transaction_is_null_non_coinbase(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_null_non_coinbase(transaction);
    return Py_BuildValue("i", res); 
}

PyObject* bitprim_native_chain_transaction_is_oversized_coinbase(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_oversized_coinbase(transaction);
    return Py_BuildValue("i", res); 
}

PyObject* bitprim_native_chain_transaction_is_immature(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    uint64_t py_target_height;

    if ( ! PyArg_ParseTuple(args, "OK", &py_transaction, &py_target_height)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_immature(transaction, py_target_height);
    return Py_BuildValue("i", res); 
}

PyObject* bitprim_native_chain_transaction_is_overspent(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_overspent(transaction);
    return Py_BuildValue("i", res); 
}

PyObject* bitprim_native_chain_transaction_is_double_spend(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    int py_include_unconfirmed;

    if ( ! PyArg_ParseTuple(args, "Oi", &py_transaction, &py_include_unconfirmed)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_double_spend(transaction, py_include_unconfirmed);
    return Py_BuildValue("i", res); 
}


PyObject* bitprim_native_chain_transaction_is_missing_previous_outputs(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_missing_previous_outputs(transaction);
    return Py_BuildValue("i", res); 
}

//int chain_transaction_is_final(transaction_t transaction, uint64_t block_height, uint32_t block_time);
PyObject* bitprim_native_chain_transaction_is_final(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    uint64_t py_block_height;
    uint32_t py_block_time;

    if ( ! PyArg_ParseTuple(args, "OKI", &py_transaction, &py_block_height, &py_block_time)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_final(transaction, py_block_height, py_block_time);
    return Py_BuildValue("i", res); 
}

PyObject* bitprim_native_chain_transaction_is_locktime_conflict(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    int res = chain_transaction_is_locktime_conflict(transaction);
    return Py_BuildValue("i", res);
}

PyObject* bitprim_native_chain_transaction_destruct(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    chain_transaction_destruct(transaction);
    Py_RETURN_NONE;
}

/*
PyObject* bitprim_native_chain_transaction_outputs(PyObject* self, PyObject* args){
    PyObject* py_transaction;
    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }
    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    output_list_t res = chain_transaction_outputs(transaction);
    return Py_BuildValue("O", res);  
    
}

PyObject* bitprim_native_chain_transaction_inputs(PyObject* self, PyObject* args){
    PyObject* py_transaction;

    if ( ! PyArg_ParseTuple(args, "O", &py_transaction)) {
        return NULL;
    }

    transaction_t transaction = (transaction_t)get_ptr(py_transaction);
    input_list_t res = chain_transaction_inputs(transaction);
    return Py_BuildValue("O", res);  
}
*/
