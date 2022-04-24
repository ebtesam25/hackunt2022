import { View, Text, Image} from "react-native";
import { Divider } from "react-native-material-ui";
import { Appbar, Button } from "react-native-paper";
import { Icon, Slider } from 'react-native-elements';
import { theme } from "../utils/theme";
import Navbar from "../components/navbar";
import { useState } from "react";
import { GooglePlacesAutocomplete } from 'react-native-google-places-autocomplete';
import { keys } from "../utils/apikeys";

export default function AddEmission ({route}) {
    const {type, subtype, icon} = route.params
    const [distance, setdistance] = useState(0)
    const [co2, setco2] = useState(0)
    
    return(
        <View style={{flex:1}}>
            <Text style={{textAlign:'center', fontWeight:'bold', paddingTop:'10%', paddingBottom:'5%', fontSize:17}}>Add Emission</Text>
            <Divider/>


            <View style={{paddingHorizontal:'5%', paddingVertical:'5%'}}>
                <Text style={{fontWeight:'bold', fontSize:17, marginBottom:'.5%'}}>{type}</Text>
                <Text style={{fontWeight:'200', fontSize:14, marginBottom:'5%', color:'#575757'}}>{subtype}</Text>
                <Text style={{fontWeight:'bold', fontSize:17, marginBottom:'.5%'}}>Distance</Text>
                <Text style={{fontWeight:'200', fontSize:14, marginBottom:'5%', color:'#575757'}}>{distance} km</Text>
                <Slider
                    value={distance}
                    onValueChange={setdistance}
                    maximumValue={10000}
                    minimumValue={0}
                    step={1}
                    allowTouchTrack
                    trackStyle={{ height: 5, backgroundColor: 'transparent' }}
                    thumbStyle={{ height: 20, width: 20, backgroundColor: 'transparent' }}
                    thumbProps={{
                    children: (
                        <Icon
                        name={icon}
                        type="ionicon"
                        size={10}
                        reverse
                        containerStyle={{ bottom: 10, right: 10 }}
                        color={theme.primary}
                        />
                    ),
                    }}
                />


                

                <Text style={{fontWeight:'bold', fontSize:17, marginBottom:'.5%'}}>Date</Text>
                <Text style={{fontWeight:'bold', fontSize:14, marginBottom:'5%', color:'#575757'}}>{new Date().getMonth().toString()}/{new Date().getDate().toString()}/{new Date().getFullYear().toString()}</Text>

                <Button onPress={()=>console.log('added')} style={{borderRadius:15, width:'95%'}} color={theme.primary} mode="outlined">Add Record</Button>

                
             
                
                




            </View>
            <Navbar/>

        </View>
    )
}