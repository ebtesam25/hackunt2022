import { View, Text, Image} from "react-native";
import { Divider } from "react-native-material-ui";
import { Appbar, Button, TextInput } from "react-native-paper";
import { CheckBox, Icon, Slider } from 'react-native-elements';
import { theme } from "../utils/theme";
import Navbar from "../components/navbar";
import { useState } from "react";
import { GooglePlacesAutocomplete } from 'react-native-google-places-autocomplete';
import { keys } from "../utils/apikeys";
import { KeyboardAwareScrollView } from "react-native-keyboard-aware-scroll-view";
import Clipboard from '@react-native-clipboard/clipboard';

export default function Group ({route}) {
    const [name, setname] = useState('')
    const [amount, setamount] = useState(0)
    const [code, setcode] = useState('')
    const [inviteCode, setinviteCode] = useState('')

    const _addGroup = () => {
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
        "action": "addgroup",
        "name": name,
        "userid": "2",
        "pool": amount
        });

        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
        };

        fetch("https://us-central1-aiot-fit-xlab.cloudfunctions.net/greenscore", requestOptions)
        .then(response => response.json())
        .then(result => {console.log(result);copyToClipboard(result.invitecode)})
        .catch(error => console.log('error', error));
    }

    const copyToClipboard = (code) => {
        Clipboard.setString(code);
      };
    
    return(
        
        <View style={{flex:1}}>
            <Text style={{textAlign:'center', fontWeight:'bold', paddingTop:'10%', paddingBottom:'5%', fontSize:17}}>Group</Text>
            <Divider/>

            <KeyboardAwareScrollView>
            <View style={{paddingHorizontal:'5%', paddingVertical:'5%'}}>
                <Text style={{fontWeight:'bold', fontSize:17, marginBottom:'.5%'}}>Create a new group</Text>
                <TextInput
                label="Name"
                mode="outlined"
                activeOutlineColor = {theme.primary}
                value={name}
                onChangeText={e => setname(e)}
                />
                <Text style={{fontWeight:'bold', fontSize:17, marginVertical:'1.5%'}}>Amount</Text>
                <Text style={{fontWeight:'200', fontSize:14, marginBottom:'5%', color:'#575757'}}>Set an amount each member must deposit into the pool for joining the group</Text>
                <Slider
                    value={amount}
                    onValueChange={setamount}
                    maximumValue={1000}
                    minimumValue={0}
                    step={1}
                    allowTouchTrack
                    trackStyle={{ height: 5, backgroundColor: 'transparent' }}
                    thumbStyle={{ height: 20, width: 20, backgroundColor: 'transparent' }}
                    thumbProps={{
                    children: (
                        <Icon
                        name="cash"
                        type="ionicon"
                        size={10}
                        reverse
                        containerStyle={{ bottom: 10, right: 10 }}
                        color={theme.primary}
                        />
                    ),
                    }}
                />

                
                <Text style={{fontWeight:'bold', fontSize:14, marginBottom:'5%', color:'#575757'}}>${amount}</Text>
                <Button style={{borderRadius:15}} icon="plus" color={theme.primary} mode="contained">Create group and copy invite code</Button>

                
                <View style={{height:1, borderColor:"#EAEAEA", borderWidth:1, marginVertical:'5%'}}><Text>OR</Text></View>
                <Text style={{fontWeight:'bold', fontSize:17, marginBottom:'.5%'}}>Join an existing group</Text>
                <Text style={{fontWeight:'200', fontSize:14, marginBottom:'5%', color:'#575757'}}>Paste your invite code below to join an existing group</Text>
                <TextInput label="Invite Code" activeOutlineColor={theme.primary} mode="outlined" placeholder="Invite Code" value={code} onChangeText={(e)=>setcode(e)}></TextInput>
                <Button style={{borderRadius:15, marginVertical:'5%', borderColor:theme.primary, borderWidth:2}} icon="plus" color={theme.primary} mode="outlined">Join group</Button>

                <Text style={{color:'#575757', textAlign:'left'}}>By joining a group, you agree to the terms and conditions set by the group lead and GreenScore</Text>



                
             
                
                




            </View>
            </KeyboardAwareScrollView>
            <Navbar/>

        </View>
        
    )
}