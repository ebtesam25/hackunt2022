import { useNavigation } from "@react-navigation/native";
import { View, Image, Text } from "react-native";
import { Button, BottomNavigation } from "react-native-paper";
import Navbar from "../components/navbar";
import { theme } from "../utils/theme";

export default function Register (){
    const navigation = useNavigation();
    return(
        <View style={{backgroundColor:"#FFF", flex:1}}>
        <View style={{alignSelf:'center', alignItems:'center', paddingHorizontal:'5%', paddingTop:'15%'}}>
            <Image source={require('../assets/logo.png')}></Image>
            <View style={{marginTop:'35%'}}></View>
            <Text style={{fontWeight:'bold', textAlign:'center', fontSize:25}}>Hi there 👋</Text>
            <View style={{width:'90%'}}>
            <Text style={{textAlign:'center'}}>Thanks for joining our fight against climate change!</Text>
            <Text style={{textAlign:'center'}}>To start tracking your CO2 emissions, tap the button below.</Text>
            </View>
            <View style={{marginTop:'35%'}}></View>
            <Button icon="lightning-bolt" style={{borderRadius:20, width:350, backgroundColor:theme.primary, marginBottom:'5%'}} mode="contained" onPress={() => navigation.navigate('Emmission')}>Track my emissions</Button>
            <Button icon="plus" color={theme.primary} style={{borderRadius:20, width:350, borderColor:theme.primary, borderWidth:2, backgroundColor:theme.white}} mode="outlined" onPress={() => navigation.navigate('Group')}>Create or join a group</Button>
        </View>
        <Navbar/>
        </View>
    )
}