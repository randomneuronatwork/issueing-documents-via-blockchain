pragma solidity >=0.4.22 <0.6.0;
contract user{
    
    string  document_name;
    string  issuing_authority;
    string  file;
    
    
    event Info(
string document_name,
string issuing_authority,
string file
    
);
    
    
    
    
    
    
    
    
    function upload_doc(string  memory doc_name,string  memory issuing_auth, string  memory doc) public{
        document_name=doc_name;
        issuing_authority=issuing_auth;
        file=doc;
        emit Info(doc_name,issuing_auth,doc);
        
    }

        
        
        
        
    
}