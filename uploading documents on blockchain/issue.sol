pragma solidity >=0.4.22 <0.6.0;
contract issue_doc{
     string public  authority_name="Maharashtra Board";
     string  public  document="Marksheet";
     string public  student_name;
     string public  seat_no;
     address payable public student_add;
     string  public  doc_body;
     uint256 amount=0;
      //constructor(address payable add) public{
      //  student_add=add;
   // }
     
     function issue_marksheet(string memory student ,string memory seat,string memory body ,address payable add)public payable{
         
         student_name=student;
         seat_no=seat;
         student_add=add;
         doc_body=body;
         student_add.transfer(amount);
            
         
         
        
         
         
     }
     
    
     
    
    
    
    
    
}