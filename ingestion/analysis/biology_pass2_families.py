"""Authored, disjoint competence families from the real Biology Pass 1 batch.

No confidence is authored. Unverified visual records and disputed memo records
are deliberately not members. Recall and causal mechanisms are kept separate.
"""
C='BIO-2022-CYCLE1'
H='BIO-2022-CIRC'
J='BIO-2023-JUL'
M='BIO-2023-MICRO'
N='BIO-2023-NOV'
FAMILIES = [
    {'family_id':'QUESTION-FAMILY-BIO-001', 'name':'Recognise microorganism terminology',
     'topic':'Microorganisms', 'operations':['match','identify'],
     'definition':'Match a biological description to a microorganism term, group or associated process; this is terminology recognition, not an explanation of a mechanism.',
     'members':[(J,f'1.1.row{i}') for i in range(1,11)]+[(M,f'1.row{i}') for i in range(1,11)]+[(J,'1.3.1'),(M,'3.1.1')]},
    {'family_id':'QUESTION-FAMILY-BIO-002','name':'Identify the independent variable of an investigation',
     'topic':'Experimental reasoning','operations':['identify'],
     'definition':'Identify the factor varied or compared in the stated investigation rather than the measured response.',
     'members':[(J,'4.1.2.a'),(M,'2.1'),(N,'3.2.2')]},
    {'family_id':'QUESTION-FAMILY-BIO-003','name':'Identify the measured response of an investigation',
     'topic':'Experimental reasoning','operations':['identify'],
     'definition':'Name the dependent variable from the investigation description, distinguishing the measurement from what is varied.',
     'members':[(J,'4.1.2.b'),(N,'1.4.5')]},
    {'family_id':'QUESTION-FAMILY-BIO-004','name':'Specify controls that keep comparisons fair',
     'topic':'Experimental reasoning','operations':['identify','describe'],
     'definition':'Name relevant quantities or participant characteristics held the same between compared groups; do not confuse controlled variables with an untreated control group.',
     'members':[(C,'2.2.4.A'),(J,'3.2.5'),(J,'4.1.2.c'),(J,'4.2.3'),(N,'1.4.6'),(N,'3.2.4')]},
    {'family_id':'QUESTION-FAMILY-BIO-005','name':'Apply water balance to urine volume and concentration',
     'topic':'Excretion','operations':['predict','explain'],
     'definition':'Use changed water intake or loss to predict urine concentration and, where asked, volume. This is an application task rather than recall of the definition of excretion.',
     'members':[(C,'1.3.4.A'),(J,'1.2.4'),(J,'1.4.5')]},
    {'family_id':'QUESTION-FAMILY-BIO-006','name':'Explain osteoarthritis through cartilage damage',
     'topic':'Skeletal system','operations':['describe','explain'],
     'definition':'Describe cartilage deterioration and its consequences at a joint; do not substitute the name of a disease for its mechanism.',
     'members':[(J,'3.2.7'),(N,'2.2.5')]},
    {'family_id':'QUESTION-FAMILY-BIO-007','name':'Distinguish controllable and uncontrollable circulatory risk factors',
     'topic':'Transport in animals','operations':['identify','distinguish'],
     'definition':'Respond to the requested controllability category in the hypertension or coronary-disease context, rather than supplying an undifferentiated list of risks.',
     'members':[(H,'4.5'),(N,'3.3.4'),(N,'3.3.5')]},
    {'family_id':'QUESTION-FAMILY-BIO-008','name':'Link oxygen delivery to cellular energy demands',
     'topic':'Transport in animals','operations':['explain cause and effect'],
     'definition':'Explain the consequence of altered oxygen delivery or demand using respiration/energy, in the malaria and exercise contexts. Not a terminology-recall family.',
     'members':[(M,'3.1.5'),(N,'1.4.1')]},
    {'family_id':'QUESTION-FAMILY-BIO-009','name':'State a conclusion from a biological comparison',
     'topic':'Data interpretation','operations':['conclude','compare'],
     'definition':'State the relationship supported by the supplied group or age data rather than restating an isolated measurement.',
     'members':[(C,'2.2.4.B'),(J,'4.2.5'),(N,'3.2.5')]},
]
